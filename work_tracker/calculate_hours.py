import glob
import re
import os
from datetime import datetime, timedelta
import math

# Costanti
TARGET_HOURS = 275
HOURS_PER_DAY = 6
DAILY_REPORT_PATTERN = r'^\d{2}-\d{2}\.md$' # Pattern per i nomi dei file MM-DD.md
LABOR_HOURS_MARKER = "Orari Lavorativi"

def extract_hours_from_file(filepath):
    """Estrae le ore totali lavorate da un singolo file Markdown."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            # Cerchiamo la riga che inizia con "| Orari Lavorativi"
            if line.strip().startswith(f'| {LABOR_HOURS_MARKER}'):
                # Dividiamo la riga per il separatore di colonna '|'
                parts = [part.strip() for part in line.split('|')]
                # L'ultima parte non vuota dovrebbe contenere il totale
                # Cerchiamo l'ultimo elemento non vuoto/whitespace dalla fine
                for part in reversed(parts):
                    if part: # Se la parte non è vuota
                         try:
                            # Convertiamo in intero
                            hours = int(part)
                            return hours
                         except ValueError:
                            # Se non è un numero, potrebbe essere la colonna 'Totale'
                            # o un altro errore di parsing. Saltiamo questa parte.
                            continue
                # Se arriviamo qui, abbiamo trovato la riga ma non il numero finale
                print(f"Attenzione: Trovata riga '{LABOR_HOURS_MARKER}' in {filepath}, ma non è stato possibile estrarre un numero totale.")
                return 0 # Ritorniamo 0 per questo file se non riusciamo a parse
        # Se il loop finisce e non troviamo la riga
        print(f"Attenzione: Riga '{LABOR_HOURS_MARKER}' non trovata in {filepath}.")
        return 0 # Ritorniamo 0 se la riga non è presente

    except FileNotFoundError:
        print(f"Errore: File non trovato - {filepath}")
        return 0
    except Exception as e:
        print(f"Errore durante la lettura o parsing di {filepath}: {e}")
        return 0

def calculate_working_days(start_date, num_working_days):
    """Calcola la data finale aggiungendo un numero specifico di giorni lavorativi
       (Lun-Ven) a partire da una data iniziale."""
    current_date = start_date
    days_added = 0
    working_days_found = 0

    # Continua finché non abbiamo trovato il numero richiesto di giorni lavorativi
    while working_days_found < num_working_days:
        # current_date.weekday() restituisce: 0=Lunedì, 1=Martedì, ..., 5=Sabato, 6=Domenica
        if current_date.weekday() < 5: # Se è Lunedì (0) fino a Venerdì (4)
            working_days_found += 1

        # Se abbiamo trovato abbastanza giorni lavorativi, non incrementare più la data
        if working_days_found < num_working_days:
             current_date += timedelta(days=1)
             days_added += 1
        else:
            # Abbiamo trovato l'ultimo giorno lavorativo necessario.
            # La data corrente è la data di fine. Usciamo dal loop.
            pass


    return current_date

# --- Main Execution ---
if __name__ == "__main__":
    total_hours_worked = 0
    processed_files = []

    # Trova tutti i file che corrispondono al pattern MM-DD.md nella directory corrente
    # Usiamo una regex più precisa oltre a glob per evitare file come 06-03.md.backup
    all_md_files = glob.glob('*.md')
    daily_report_files = [f for f in all_md_files if re.match(DAILY_REPORT_PATTERN, os.path.basename(f))]


    if not daily_report_files:
        print("Nessun file giornaliero (MM-DD.md) trovato nella directory corrente.")
    else:
        print("Elaborazione dei file giornalieri...")
        for filename in sorted(daily_report_files): # Ordina per data per una migliore visualizzazione
            hours = extract_hours_from_file(filename)
            print(f"- {filename}: {hours} ore")
            total_hours_worked += hours
            processed_files.append(filename)

        print("-" * 20)
        print(f"Totale ore lavorate finora: {total_hours_worked} ore")

    print(f"Obiettivo ore totali di tirocinio: {TARGET_HOURS} ore")

    remaining_hours = TARGET_HOURS - total_hours_worked

    if remaining_hours <= 0:
        print("\nObiettivo di ore già raggiunto o superato! 🎉")
    else:
        print(f"\nOre rimanenti per raggiungere l'obiettivo: {remaining_hours} ore")

        # Calcolo dei giorni lavorativi necessari
        # Arrotondiamo per eccesso perché anche un'ora residua richiede un giorno
        working_days_needed = math.ceil(remaining_hours / HOURS_PER_DAY)
        print(f"Giorni lavorativi (Lun-Ven) necessari, lavorando {HOURS_PER_DAY} ore/giorno: {working_days_needed} giorni")

        # Richiedi la data di inizio per la proiezione
        while True:
            start_date_str = input("\nInserisci la data di inizio per la proiezione (formato YYYY-MM-DD): ")
            try:
                projection_start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
                break # Esci dal loop se il formato è corretto
            except ValueError:
                print("Formato data non valido. Usa YYYY-MM-DD (es. 2024-06-05).")

        # Calcola la data di fine
        projected_end_date = calculate_working_days(projection_start_date, working_days_needed)

        print("\n--- Prospetto Data Finale ---")
        print(f"Iniziando la proiezione da: {projection_start_date.strftime('%Y-%m-%d')}")
        print(f"Lavorando {HOURS_PER_DAY} ore al giorno (Lun-Ven)")
        print(f"Necessari ancora {working_days_needed} giorni lavorativi")
        print(f"Data finale prevista del tirocinio: {projected_end_date.strftime('%Y-%m-%d')}")
