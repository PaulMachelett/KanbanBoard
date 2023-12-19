import React, { useState, useEffect } from "react";
import PopupExample from "./popUP.js";
import { Container, IconButton, TextField } from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import CreateKanbanCardButton from "../kanbancard/CreateKanbanCardButton.js";
import Kanbancard from "../kanbancard/KanbanCard.js";
import { createApiPhase, deleteApiPhase } from "../../lib/api/call.js";

const KanbanBoard = ({ phases: initialPhases }) => {
  const [phases, setPhases] = useState([]);

  useEffect(() => {
    setPhases(initialPhases);
  }, [initialPhases]);

  const addPhase = async (phasenname) => {
    const data = {
      "id": 1,
      "name": phasenname,
      "projectid": "1"
    };

    const phaseId = 1;
    try {
      // Make the API call
      const response = await createApiPhase(data,phaseId);
  
      if (response && response.ok) {
        // If the response is defined and ok, update the state or perform any other necessary actions
        const responseData = await response.json();
        setPhases((prevPhases) => [...prevPhases, responseData]);
      } else {
        console.error("Failed to create phase:", response ? response.statusText : "Response is undefined");
      }
    } catch (error) {
      console.error("Error:", error.message);
    }
  };


  const deletePhase = () => {
    deleteApiPhase(phases.id)
  };
  // update from kanban-team
  const addCard = (phaseId, newCardText) => {
    setPhases((prevPhases) =>
      prevPhases.map((phase) =>
        phase.id === phaseId
          ? {
              ...phase,
              cards: [...phase.cards, { id: Date.now(), text: newCardText }],
            }
          : phase
      )
    );
  };

  return (
    <Container
      sx={{
        flexDirection: "column",
      }}
    >
      {phases.map((phase) => (
        <Container
          style={{
            border: "1px",
            borderRadius: "32px",
            padding: "10px",
            margin: "10px",
            display: "flex",
            flexDirection: "column",
            alignItems: "center", // Zentriert die Kinder horizontal
          }}
          sx={{
            bgcolor: "grey.200",
          }}
          key={phase.id}
        >
          <h1></h1>
          <Container
            style={{
              display: "flex",
              alignItems: "center",
              gap: "1rem",
              flexWrap: "wrap",
            }}
            key={phase.id}
          >
            <h3>{phase.name}</h3>
            <PopupExample />

            <IconButton onClick={() => deletePhase(phase.id)}>
              <DeleteIcon />
            </IconButton>
          </Container>
          <Kanbancard />
          <Container style={{ marginTop: "10px" }}>
            <CreateKanbanCardButton />
          </Container>
        </Container>
      ))}

      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "40",
        }}
      >
        <TextField
        sx={{}}
        type="text"
        placeholder="Phasennamen"
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            
            addPhase(e.target.value);
            e.target.value = "";
          }
        }}/>
        
      </div>
    </Container>
  );
};
export default KanbanBoard;
