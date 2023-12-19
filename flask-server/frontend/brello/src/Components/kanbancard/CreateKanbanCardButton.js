import React, { useState } from "react";
import Button from "@mui/material/Button";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";

const CreateKanbanCardButton = ({ onCardCreated }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newCard, setNewCard] = useState({
    cardtitle: "",
    cardcontent: "",
    card_creator: "",
    card_storypoints: "",
    assigned_person: "",
    card_end_date: "",
  });

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setNewCard({
      cardtitle: "",
      cardcontent: "",
      card_creator: "",
      card_storypoints: "",
      assigned_person: "",
      card_end_date: "",
    });
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewCard({ ...newCard, [name]: value });
  };

  const handleCreateCard = () => {
    const newDate = null;

    fetch("http://127.0.0.1:5000/kanbancard", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        id: null,
        timestamp: newDate,
        cardtitle: newCard.cardtitle,
        cardcontent: newCard.cardcontent,
        card_phase_id: null,
        card_start_date: newDate,
        card_end_date: newDate,
        card_creator: null,
        card_storypoints: null,
        assigned_person: null,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Card created successfully", data);
        onCardCreated();
        closeModal();
      })
      .catch((error) => console.error("Error creating card:", error));
  };

  return (
    <div>
      <Button
        variant="contained"
        color="primary"
        onClick={openModal}
        style={{ margin: "20px", padding: 10 }}
      >
        Create New Kanban Card
      </Button>

      <Modal
        open={isModalOpen}
        onClose={closeModal}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box
          sx={{
            position: "absolute",
            top: "50%",
            left: "50%",
            transform: "translate(-50%, -50%)",
            width: 500,
            bgcolor: "background.paper",
            boxShadow: 24,
            p: 4,
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Typography variant="h6" component="div">
            Create New Kanban Card
          </Typography>
          <br></br>
          <br></br>
          <TextField
            label="Card Title"
            variant="outlined"
            name="cardtitle"
            value={newCard.cardtitle}
            onChange={handleInputChange}
          />
          <br />
          <br />
          <TextField
            label="Card Content"
            variant="outlined"
            name="cardcontent"
            value={newCard.cardcontent}
            onChange={handleInputChange}
          />
          <br />
          <br />
          <TextField
            label="Assigned Person"
            variant="outlined"
            name="assigned_person"
            value={newCard.assigned_person}
            onChange={handleInputChange}
          />
          <br />
          <br />
          <Button
            variant="contained"
            color="primary"
            onClick={handleCreateCard}
          >
            Create Card
          </Button>
          <br />
          <br />
          <Button
            variant="contained"
            color="secondary"
            onClick={closeModal}
          >
            Cancel
          </Button>
        </Box>
      </Modal>
    </div>
  );
};

export default CreateKanbanCardButton;
