import { Button, IconButton, TextField } from "@mui/material";
import React, { useState } from "react";
import SettingsIcon from '@mui/icons-material/Settings';

const PopupExample = ({ phases, setPhases }) => {
  const [showPopup, setShowPopup] = useState(false);
  const [phaseIdToUpdate, setPhaseIdToUpdate] = useState(null);

  const openPopup = (id) => {
    setPhaseIdToUpdate(id);
    setShowPopup(true);
  };

  const closePopup = () => {
    setShowPopup(false);
    setPhaseIdToUpdate(null);
  };

  const updatePhaseTitle = (newTitle) => {
    if (phaseIdToUpdate !== null) {
      setPhases((prevPhases) =>
        prevPhases.map((phase) =>
          phase.id === phaseIdToUpdate ? { ...phase, title: newTitle } : phase
        )
      );
      closePopup();
    }
  };

  return (
    <>
    <IconButton onClick={() => openPopup(/* pass the phase ID to update */)}>
       <SettingsIcon/>
      </IconButton>
      {showPopup && (
        <div className="popup">
          <div className="popup-content">
            <TextField
              sx={{}}
              type="text"
              placeholder="Phasennamen ändern"
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  updatePhaseTitle(e.target.value);
                  e.target.value = "";
                }
              }}
            />

            <Button variant="contained" color="grey" onClick={closePopup}>
              Schließen
            </Button>
          </div>
        </div>
      )}
    </>
  );
};

export default PopupExample;
