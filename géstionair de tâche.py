class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Complétée" if self.completed else "En cours"
        return f"{self.description} - Date d'échéance: {self.due_date} - Statut: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)
        print("Tâche ajoutée avec succès!")

    def list_tasks(self, show_completed=True):
        if not self.tasks:
            print("Aucune tâche trouvée.")
            return
        for task in self.tasks:
            if show_completed or not task.completed:
                print(task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                print("Tâche marquée comme complétée!")
                return
        print("Tâche non trouvée.")

    def delete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                print("Tâche supprimée avec succès!")
                return
        print("Tâche non trouvée.")

def main():
    manager = TaskManager()
    while True:
        print("\n--- Gestionnaire de Tâches ---")
        print("1. Ajouter une tâche")
        print("2. Lister les tâches")
        print("3. Marquer une tâche comme complétée")
        print("4. Supprimer une tâche")
        print("5. Quitter")
        choice = input("Choisissez une option: ")

        if choice == '1':
            description = input("Entrez la description de la tâche: ")
            due_date = input("Entrez la date d'échéance (format: YYYY-MM-DD): ")
            manager.add_task(description, due_date)
        elif choice == '2':
            show_completed = input("Voulez-vous afficher les tâches complétées? (oui/non): ").lower() == 'oui'
            manager.list_tasks(show_completed)
        elif choice == '3':
            description = input("Entrez la description de la tâche à marquer comme complétée: ")
            manager.mark_task_completed(description)
        elif choice == '4':
            description = input("Entrez la description de la tâche à supprimer: ")
            manager.delete_task(description)
        elif choice == '5':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
