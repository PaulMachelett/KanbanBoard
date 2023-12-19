import React from 'react';
import TextField from '@mui/material/TextField';

// CommentInput-Komponente: Eingabefeld für Kommentare
const CommentInput = ({ comment, setComment, isEditing }) => {
  // Stil für das Eingabefeld. Ändert sich, wenn der Bearbeitungsmodus aktiv ist
  const inputStyle = isEditing 
    ? { width: '100%', backgroundColor: 'white', borderRadius: '4px', border: '2px solid #ADD9E6' } // Stil im Bearbeitungsmodus
    : { width: '100%', backgroundColor: 'white', borderRadius: '4px' }; // Standardstil

  return (
    <TextField
      id="filled-multiline-flexible"
      label="Kommentar"
      multiline 
      rows={6} 
      maxRows={40} 
      variant="filled" 
      value={comment} 
      onChange={(e) => setComment(e.target.value)} // Aktualisiert den Kommentar bei jeder Eingabe
      style={inputStyle} // Anwenden des bedingten Stils
    />
  );
};

export default CommentInput;
