import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, filename='tasks.json'):
        # Nom du fichier JSON utilisé comme base de données locale
        self.filename = filename
        # Chargement des tâches existantes dès l'instanciation
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Charge les tâches depuis le fichier JSON"""
        # Vérifie si le fichier existe pour éviter une erreur à la première exécution
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                # Désérialise le JSON en liste Python
                return json.load(f)
        # Retourne une liste vide si le fichier n'existe pas encore
        return []
    
    def save_tasks(self):
        """Sauvegarde les tâches dans le fichier JSON"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            # ensure_ascii=False pour conserver les accents
            # indent=2 pour un JSON lisible à l'œil
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)
    
    def add_task(self, description):
        """Ajoute une nouvelle tâche"""
        task = {
            # ID auto-incrémenté basé sur la longueur actuelle de la liste
            # ⚠️ Fragile si des tâches sont supprimées (IDs non séquentiels)
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,  # Toute nouvelle tâche commence non terminée
            # Horodatage de création au format lisible
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        # Ajout en fin de liste puis persistance immédiate
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
            # ✓ si terminée, ○ si en cours — indicateur visuel rapide
            status = "✓" if task['completed'] else "○"
            print(f"{status} [{task['id']}] {task['description']}")
            print(f"   Créée le : {task['created_at']}")
        print("="*60)
    
    def complete_task(self, task_id):
        """Marque une tâche comme terminée"""
        # Parcours linéaire — acceptable pour une petite liste locale
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True  # Mise à jour en mémoire
                self.save_tasks()         # Puis persistance
                print(f"✓ Tâche {task_id} marquée comme terminée !")
                return
        # Aucune tâche trouvée avec cet ID
        print(f"✗ Tâche {task_id} introuvable.")
    
    def delete_task(self, task_id):
        """Supprime une tâche"""
        # enumerate() pour accéder à l'index et supprimer proprement avec pop()
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted = self.tasks.pop(i)  # Suppression en mémoire
                self.save_tasks()             # Puis persistance
                print(f"✓ Tâche supprimée : {deleted['description']}")
                return
        print(f"✗ Tâche {task_id} introuvable.")
    
    def run(self):
        """Lance l'application avec le menu interactif"""
        # Boucle infinie — seul le choix '5' permet d'en sortir via break
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
            
            # .strip() pour ignorer les espaces accidentels en début/fin
            choice = input("\nChoisissez une option (1-5) : ").strip()
            
            if choice == '1':
                description = input("Description de la tâche : ").strip()
                # Validation minimale : refus des descriptions vides
                if description:
                    self.add_task(description)
                else:
                    print("✗ La description ne peut pas être vide.")
            
            elif choice == '2':
                self.list_tasks()
            
            elif choice == '3':
                # Affichage préalable pour que l'utilisateur connaisse les IDs disponibles
                self.list_tasks()
                try:
                    task_id = int(input("\nID de la tâche à marquer comme terminée : "))
                    self.complete_task(task_id)
                except ValueError:
                    # Gestion du cas où l'utilisateur saisit un non-entier
                    print("✗ ID invalide.")
            
            elif choice == '4':
                # Même logique : affichage d'abord pour guider le choix de l'ID
                self.list_tasks()
                try:
                    task_id = int(input("\nID de la tâche à supprimer : "))
                    self.delete_task(task_id)
                except ValueError:
                    print("✗ ID invalide.")
            
            elif choice == '5':
                print("\nAu revoir ! 👋")
                break  # Sortie propre de la boucle principale
            
            else:
                # Saisie hors plage 1-5
                print("✗ Option invalide. Choisissez entre 1 et 5.")

if __name__ == "__main__":
    # Point d'entrée — empêche l'exécution si le fichier est importé comme module
    app = TodoApp()
    app.run()
