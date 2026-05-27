import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Charge les tâches depuis le fichier JSON"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    def save_tasks(self):
        """Sauvegarde les tâches dans le fichier JSON"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)
    
    def add_task(self, description):
        """Ajoute une nouvelle tâche"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Tâche ajoutée : {description}")
    
    def list_tasks(self):
        """Affiche toutes les tâches"""
        if not self.tasks:
            print("\nAucune tâche dans la liste.")
            return
        
        print("\n" + "="*60)
        print("LISTE DES TÂCHES")
        print("="*60)
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"{status} [{task['id']}] {task['description']}")
            print(f"   Créée le : {task['created_at']}")
        print("="*60)
    
    def complete_task(self, task_id):
        """Marque une tâche comme terminée"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"✓ Tâche {task_id} marquée comme terminée !")
                return
        print(f"✗ Tâche {task_id} introuvable.")
    
    def delete_task(self, task_id):
        """Supprime une tâche"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted = self.tasks.pop(i)
                self.save_tasks()
                print(f"✓ Tâche supprimée : {deleted['description']}")
                return
        print(f"✗ Tâche {task_id} introuvable.")
    
    def run(self):
        """Lance l'application avec le menu interactif"""
        while True:
            print("\n" + "="*60)
            print("TODO APP - MENU PRINCIPAL")
            print("="*60)
            print("1. Ajouter une tâche")
            print("2. Afficher les tâches")
            print("3. Marquer une tâche comme terminée")
            print("4. Supprimer une tâche")
            print("5. Quitter")
            print("="*60)
            
            choice = input("\nChoisissez une option (1-5) : ").strip()
            
            if choice == '1':
                description = input("Description de la tâche : ").strip()
                if description:
                    self.add_task(description)
                else:
                    print("✗ La description ne peut pas être vide.")
            
            elif choice == '2':
                self.list_tasks()
            
            elif choice == '3':
                self.list_tasks()
                try:
                    task_id = int(input("\nID de la tâche à marquer comme terminée : "))
                    self.complete_task(task_id)
                except ValueError:
                    print("✗ ID invalide.")
            
            elif choice == '4':
                self.list_tasks()
                try:
                    task_id = int(input("\nID de la tâche à supprimer : "))
                    self.delete_task(task_id)
                except ValueError:
                    print("✗ ID invalide.")
            
            elif choice == '5':
                print("\nAu revoir ! 👋")
                break
            
            else:
                print("✗ Option invalide. Choisissez entre 1 et 5.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
