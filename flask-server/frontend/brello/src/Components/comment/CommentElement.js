import React, { useState } from 'react';
import IconButton from '@mui/material/IconButton';
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
import SaveIcon from '@mui/icons-material/Save';
import EditIcon from '@mui/icons-material/Edit';
import CommentInput from './CommentInput';

// Komponente für die Kommentarsektion
const CommentSection = () => {
  // State-Hooks für Kommentar, gespeicherten Kommentar und Bearbeitungsstatus
  const [comment, setComment] = useState('');
  const [savedComment, setSavedComment] = useState('');
  const [isEditing, setIsEditing] = useState(false);

  // Funktion zum Löschen des aktuellen und gespeicherten Kommentars
  const handleClearClick = () => {
    setComment('');
    setSavedComment('');
    setIsEditing(false);
  };

  // Funktion zum Speichern des aktuellen Kommentars
  const handleSaveClick = () => {
    setSavedComment(comment);
    setIsEditing(false);
  };

  // Funktion zum Bearbeiten des gespeicherten Kommentars
  const handleEditClick = () => {
    setComment(savedComment);
    setIsEditing(true);
  };

  // Render-Methode der Komponente
  return (
    <div style={{ display: 'flex', alignItems: 'flex-start', gap: '8px' }}>
      {/* CommentInput-Komponente mit Props für Kommentar, Setzen des Kommentars und Bearbeitungsstatus */}
      <CommentInput 
        comment={isEditing ? comment : savedComment}
        setComment={setComment}
        isEditing={isEditing} 
      />
      {/* Container für die IconButtons zum Speichern, Bearbeiten und Löschen */}
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        {/* IconButton zum Speichern von Kommentaren */}
        <IconButton onClick={handleSaveClick} style={{ ...iconButtonTheme, marginBottom: '8px' }}>
          <SaveIcon />
        </IconButton>
        {/* IconButton zum Bearbeiten von Kommentaren */}
        <IconButton onClick={handleEditClick} style={{ ...iconButtonTheme, marginBottom: '8px' }}>
          <EditIcon />
        </IconButton>
        {/* IconButton zum Löschen von Kommentaren */}
        <IconButton onClick={handleClearClick} style={iconButtonTheme}>
          <DeleteForeverIcon />
        </IconButton>
      </div>
    </div>
  );
};

// Stil-Definition für die IconButtons
const iconButtonTheme = {
  backgroundColor: 'rgba(0, 0, 0, 0.1)', 
  borderRadius: '50%',
  marginBottom: '8px',
};

export default CommentSection;
