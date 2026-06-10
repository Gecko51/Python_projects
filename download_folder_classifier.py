import os
import shutil
from pathlib import Path

# ─── Configuration ────────────────────────────────────────────────────────────
# Modifie ce chemin si nécessaire
DOWNLOADS = Path.home() / "Downloads"

# Mapping extension → nom du dossier cible
CATEGORIES = {
    # Images
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico", ".bmp", ".tiff"],
    # Vidéos
    "Vidéos": [".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv", ".wmv"],
    # Audio
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    # Documents
    "Documents": [".pdf", ".doc", ".docx", ".odt", ".txt", ".rtf", ".md"],
    # Tableurs
    "Tableurs": [".xls", ".xlsx", ".csv", ".ods"],
    # Présentations
    "Présentations": [".ppt", ".pptx", ".key"],
    # Archives
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    # Code
    "Code": [".py", ".js", ".ts", ".html", ".css", ".json", ".xml", ".yaml", ".yml", ".sh", ".sql"],
    # Exécutables / Installeurs
    "Installeurs": [".exe", ".dmg", ".pkg", ".deb", ".msi", ".appimage"],
    # Polices
    "Polices": [".ttf", ".otf", ".woff", ".woff2"],
}
# ──────────────────────────────────────────────────────────────────────────────


def get_category(extension: str) -> str:
    """Retourne le nom du dossier cible pour une extension donnée."""
    ext = extension.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Autres"  # Fallback si l'extension n'est pas reconnue


def organize_downloads(dry_run: bool = False):
    """
    Classe les fichiers du dossier Téléchargements.
    
    dry_run=True  → affiche ce qui serait fait SANS déplacer les fichiers
    dry_run=False → déplace réellement les fichiers
    """
    moved = 0
    skipped = 0

    for item in DOWNLOADS.iterdir():
        # On ignore les dossiers et les fichiers cachés (ex: .DS_Store)
        if item.is_dir() or item.name.startswith("."):
            skipped += 1
            continue

        category = get_category(item.suffix)
        target_dir = DOWNLOADS / category

        if dry_run:
            print(f"[SIMULATION] {item.name}  →  {category}/")
            continue

        # Crée le dossier cible s'il n'existe pas
        target_dir.mkdir(exist_ok=True)

        target_path = target_dir / item.name

        # Gère les doublons : renomme si un fichier du même nom existe déjà
        counter = 1
        while target_path.exists():
            stem = item.stem
            suffix = item.suffix
            target_path = target_dir / f"{stem}_{counter}{suffix}"
            counter += 1

        shutil.move(str(item), str(target_path))
        print(f"✓ {item.name}  →  {category}/")
        moved += 1

    print(f"\n{'[SIMULATION] ' if dry_run else ''}Terminé : {moved} fichiers déplacés, {skipped} ignorés.")


if __name__ == "__main__":
    # Lance d'abord en simulation pour vérifier
    # organize_downloads(dry_run=True)
    
    # Puis décommente la ligne ci-dessous pour exécuter pour de vrai
    organize_downloads(dry_run=False)
