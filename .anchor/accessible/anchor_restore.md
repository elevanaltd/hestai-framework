# ANCHOR RESTORE PROTOCOL

**CRITICAL**: Your operational context has been compacted. You must reconstruct your state from your Odyssean Anchor files. This is NOT a role reload - you are restoring your existing session state.

## ANCHOR LOCATION
Your anchor files are located in the accessible anchor directory:
- **Identity Context**: `.anchor/accessible/current/identity_context.oct.md` (SILVER primer with SHANK+ARM+FLUKE synthesis)
- **Project Context**: `.anchor/accessible/current/project_context.md` (project state snapshot)

## RESTORE ACTIONS

### STEP 1: Read Your Anchor Files
- FULLY PROCESS `.anchor/accessible/current/identity_context.oct.md` to restore your role state and capabilities
- FULLY READ `.anchor/accessible/current/project_context.md` to restore your understanding of the project
- Pay special attention to the **ANCHOR_INTEGRATION** section in project context for reconstruction notes

### STEP 2: Reconstruct Your Session State
- Follow the reconstruction instructions in your project context's **ANCHOR_INTEGRATION** section
- Restore your understanding of:
  - Your role and capabilities (from identity context)
  - Current project status and progress
  - Technical decisions and context you had established
  - Current session goals and next steps

### STEP 3: Extract Validation Key
- From your `identity_context.oct.md` file, locate the **VALIDATION_KEY** at the bottom
- This key proves you have successfully read and understood your identity context

### STEP 4: Signal Completion & Resume
- Once you have fully reconstructed your context from your anchor files
- Execute the final command to resume the system: `.anchor/accessible/bin/anchor-restore --complete [VALIDATION_KEY]`

### STEP 5: Resume Work
- Continue with your development work from where you left off
- Check your `project_context.md` for the **CURRENT_WORK** section to see what's next

## VALIDATION
To prove successful reconstruction, you must extract the validation key from your identity context and use it to complete the restore process.