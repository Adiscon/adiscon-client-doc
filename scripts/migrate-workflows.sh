#!/bin/bash

# Migration script for combined documentation workflow
# This script helps migrate from separate HTML/PDF workflows to the combined workflow

set -e

echo "🚀 Documentation Workflow Migration Script"
echo "==========================================="
echo ""

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Error: This script must be run from within a git repository"
    exit 1
fi

# Check if the new combined workflow exists
if [ ! -f ".github/workflows/pr-build-docs-combined.yml" ]; then
    echo "❌ Error: Combined workflow file not found at .github/workflows/pr-build-docs-combined.yml"
    echo "Please ensure the combined workflow has been created first."
    exit 1
fi

echo "✅ Found combined workflow file"

# Check for old workflow files
OLD_HTML_WORKFLOW=".github/workflows/pr-build-docs.yml"
OLD_PDF_WORKFLOW=".github/workflows/pr-build-docs-pdf.yml"

FOUND_OLD_WORKFLOWS=false

if [ -f "$OLD_HTML_WORKFLOW" ]; then
    echo "📄 Found old HTML workflow: $OLD_HTML_WORKFLOW"
    FOUND_OLD_WORKFLOWS=true
fi

if [ -f "$OLD_PDF_WORKFLOW" ]; then
    echo "📄 Found old PDF workflow: $OLD_PDF_WORKFLOW"
    FOUND_OLD_WORKFLOWS=true
fi

if [ "$FOUND_OLD_WORKFLOWS" = false ]; then
    echo "ℹ️  No old workflow files found - migration may already be complete"
else
    echo ""
    echo "🔍 Migration Status Check"
    echo "========================"
    echo ""
    
    # Check current branch
    CURRENT_BRANCH=$(git branch --show-current)
    echo "Current branch: $CURRENT_BRANCH"
    
    # Check if there are any open PRs (we can't check this automatically, so we'll just remind the user)
    echo ""
    echo "⚠️  IMPORTANT: Before proceeding with migration:"
    echo "   1. Test the new combined workflow on a test PR"
    echo "   2. Verify both HTML and PDF builds work correctly"
    echo "   3. Check that artifacts are properly combined"
    echo "   4. Ensure GitHub Pages deployment works"
    echo "   5. Update any branch protection rules if necessary"
    echo ""
    
    read -p "Have you tested the new workflow and confirmed it works? (y/N): " -r
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo ""
        echo "🛑 Migration halted. Please test the new workflow first:"
        echo "   1. Create a test PR with some documentation changes"
        echo "   2. Verify the combined workflow runs successfully" 
        echo "   3. Check that both HTML and PDF documentation are built"
        echo "   4. Confirm the preview site works correctly"
        echo "   5. Re-run this script when testing is complete"
        echo ""
        exit 0
    fi
fi

echo ""
echo "🔧 Migration Actions"
echo "==================="
echo ""

# Function to safely remove old workflows
remove_old_workflows() {
    echo "Removing old workflow files..."
    
    if [ -f "$OLD_HTML_WORKFLOW" ]; then
        echo "  - Removing $OLD_HTML_WORKFLOW"
        git rm "$OLD_HTML_WORKFLOW" 2>/dev/null || rm "$OLD_HTML_WORKFLOW"
    fi
    
    if [ -f "$OLD_PDF_WORKFLOW" ]; then
        echo "  - Removing $OLD_PDF_WORKFLOW"
        git rm "$OLD_PDF_WORKFLOW" 2>/dev/null || rm "$OLD_PDF_WORKFLOW"
    fi
    
    echo "✅ Old workflow files removed"
}

# Function to create a migration commit
create_migration_commit() {
    echo "Creating migration commit..."
    
    # Stage the combined workflow if it's not already staged
    git add .github/workflows/pr-build-docs-combined.yml 2>/dev/null || true
    
    # Stage removal of old workflows
    if [ -f "$OLD_HTML_WORKFLOW" ]; then
        git add "$OLD_HTML_WORKFLOW" 2>/dev/null || true
    fi
    if [ -f "$OLD_PDF_WORKFLOW" ]; then
        git add "$OLD_PDF_WORKFLOW" 2>/dev/null || true
    fi
    
    # Add README if it exists
    if [ -f "README.COMBINED-WORKFLOW.md" ]; then
        git add "README.COMBINED-WORKFLOW.md" 2>/dev/null || true
    fi
    
    # Check if there are any changes to commit
    if git diff --cached --quiet; then
        echo "ℹ️  No changes to commit"
    else
        COMMIT_MSG="Migrate to combined documentation workflow

- Replace separate HTML and PDF workflows with combined parallel workflow
- Fix GitHub Actions v4 artifact naming conflicts
- Improve build performance with parallel execution
- Enhance user experience with unified preview site

This resolves the artifact upload conflicts where multiple jobs
tried to upload artifacts with the same name, which is no longer
allowed in GitHub Actions v4."

        git commit -m "$COMMIT_MSG"
        echo "✅ Migration commit created"
        
        echo ""
        echo "📋 Next steps:"
        echo "  1. Push this commit: git push origin $CURRENT_BRANCH"
        echo "  2. Create a PR to test the migration"
        echo "  3. Update branch protection rules if needed"
        echo "  4. Monitor the first few workflow runs"
    fi
}

# Ask user what they want to do
echo "Choose migration action:"
echo "  1) Remove old workflows and create migration commit"
echo "  2) Just remove old workflows (no commit)"
echo "  3) Show what would be removed (dry run)"
echo "  4) Cancel migration"
echo ""
read -p "Enter your choice (1-4): " -r CHOICE

case $CHOICE in
    1)
        echo ""
        remove_old_workflows
        create_migration_commit
        ;;
    2)
        echo ""
        remove_old_workflows
        echo ""
        echo "ℹ️  Old workflows removed. You can now commit these changes manually:"
        echo "   git add -A"
        echo "   git commit -m 'Remove old separate documentation workflows'"
        ;;
    3)
        echo ""
        echo "🔍 Dry run - files that would be removed:"
        if [ -f "$OLD_HTML_WORKFLOW" ]; then
            echo "  - $OLD_HTML_WORKFLOW"
        fi
        if [ -f "$OLD_PDF_WORKFLOW" ]; then
            echo "  - $OLD_PDF_WORKFLOW"
        fi
        if [ ! -f "$OLD_HTML_WORKFLOW" ] && [ ! -f "$OLD_PDF_WORKFLOW" ]; then
            echo "  - No old workflow files found to remove"
        fi
        echo ""
        echo "📄 Combined workflow location:"
        echo "  - .github/workflows/pr-build-docs-combined.yml"
        ;;
    4)
        echo ""
        echo "🛑 Migration cancelled"
        exit 0
        ;;
    *)
        echo ""
        echo "❌ Invalid choice. Migration cancelled."
        exit 1
        ;;
esac

echo ""
echo "🎉 Migration process complete!"
echo ""
echo "📚 For more information, see:"
echo "   - README.COMBINED-WORKFLOW.md (migration guide)"
echo "   - .github/workflows/pr-build-docs-combined.yml (new workflow)"
echo ""
echo "💡 Remember to update any references to the old workflow names in:"
echo "   - Branch protection rules"
echo "   - Documentation"
echo "   - README files"
echo "   - Issue templates"
echo ""