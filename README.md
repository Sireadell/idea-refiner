# Create a new directory for your project
mkdir idea-refiner
cd idea-refiner

# Initialize git
git init

# Add your files
cp path/to/refiners.py .
echo ".env\n__pycache__/\n*.pyc" > .gitignore
echo "# IdeaRefiner\n[Your README content]" > README.md
echo "sentient-agent-framework\nfireworks-ai\npython-dotenv" > requirements.txt

# Commit
git add refiners.py .gitignore README.md requirements.txt
git commit -m "Initial commit: IdeaRefiner agent for idea refinement"

# Create a new GitHub repo (e.g., Sireadell/Idea-Refiner) via GitHub UI, then:
git remote add origin https://github.com/Sireadell/Idea-Refiner.git
git push -u origin main
