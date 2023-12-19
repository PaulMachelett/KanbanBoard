import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';

const CommentElement = () => {
  const [comment, setComment] = useState('');

  const handleClearClick = () => {
    setComment(''); 
  };

  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
      <TextField
        id="filled-multiline-flexible"
        label="Kommentar"
        multiline
        rows={6}
        maxRows={40}
        variant="filled"
        value={comment}
        onChange={(e) => setComment(e.target.value)}
        style={{ 
          width: '100%', 
          backgroundColor: 'white',
          borderRadius: '4px',
        }}
      />
      <IconButton
        onClick={handleClearClick}
        style={{
          backgroundColor: 'rgba(0, 0, 0, 0.1)', 
          borderRadius: '50%', 
        }}
      >
        <DeleteForeverIcon />
      </IconButton>
    </div>
  );
};

export default CommentElement;
