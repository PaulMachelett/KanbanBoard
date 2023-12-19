import React, { useState } from "react";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";
import TextField from "@mui/material/TextField";
import jsonData from "./path/to/dummy_data.json"; // Pfade anpassen

const Kanbancard2 = () => {
  const [kanbancards, setKanbancards] = useState([]);
  const [selectedCard, setSelectedCard] = useState(null);
  const [editedCard, setEditedCard] = useState(null);

  // Dummy-Daten von der JSON-Datei
  const dummyData = jsonData;

  // Initialisierung der Karten
  useState(() => {
    setKanbancards(dummyData);
  }, []);

  const openCardInWindow = (cardId) => {
    const cardToEdit = kanbancards.find((card) => card.id === cardId);
    setSelectedCard(cardToEdit);
    setEditedCard({ ...cardToEdit });
  };

  const closeCardModal = () => {
    setSelectedCard(null);
    setEditedCard(null);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setEditedCard({ ...editedCard, [name]: value });
  };

  const handleSubmit = () => {
    const updatedCards = kanbancards.map((card) =>
      card.id === editedCard.id ? editedCard : card
    );

    setKanbancards(updatedCards);

    closeCardModal();
  };

  const handleDelete = () => {
    const updatedCards = kanbancards.filter(
      (card) => card.id !== selectedCard.id
    );

    setKanbancards(updatedCards);

    closeCardModal();
  };

  return (
    <div>
      {kanbancards.length > 0 && (
        <ul
          style={{
            listStyle: "none",
            padding: 0,
            display: "flex",
            flexDirection: "column",
            gap: "10px",
            flexWrap: "wrap",
          }}
        >
          {kanbancards
            .filter((card) => card.card_phase_id === 2)
            .map((card) => (
              <Card
                key={card.id}
                style={{ margin: "10px", minWidth: "200px", maxWidth: "300px" }}
              >
                <CardContent>
                  <Typography
                    sx={{ fontSize: 14 }}
                    color="text.secondary"
                    gutterBottom
                  >
                    {card.cardtitle}
                  </Typography>
                  {/* ... rest of the card content ... */}
                </CardContent>
                <CardActions>
                  <Button size="small" onClick={() => openCardInWindow(card.id)}>
                    Open Card
                  </Button>
                </CardActions>
              </Card>
            ))}
        </ul>
      )}

      <Modal
        open={selectedCard !== null}
        onClose={closeCardModal}
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
          }}
        >
          {selectedCard && (
            <div
            style={{
              display: "flex",
              flexDirection: "column",
              justifyContent: "center", 
              alignItems: "center",
              bgcolor: "background.grey",
            }}
          >
              <h2>{selectedCard.cardtitle}</h2>
              <br></br>
              <TextField
                label="Card Title"
                variant="outlined"
                name="cardtitle"
                value={editedCard ? editedCard.cardtitle : ""}
                onChange={handleInputChange}></TextField>
                <br></br>
              <br></br>
              <TextField
                label="Card Content"
                variant="outlined"
                name="cardcontent"
                value={editedCard ? editedCard.cardcontent : ""}
                onChange={handleInputChange}
              />
              <br></br>
              <br></br>
              <TextField
                label="Card Creator"
                variant="outlined"
                name="card_creator"
                value={editedCard ? editedCard.card_creator : ""}
                onChange={handleInputChange}
              />
              <br></br>
              <br></br>
              <TextField
                label="Story Points"
                variant="outlined"
                name="card_storypoints"
                value={editedCard ? editedCard.card_storypoints : ""}
                onChange={handleInputChange}
              />
              <br></br>
              <br></br>
              <TextField
                label="Assigned Person"
                variant="outlined"
                name="assigned_person"
                value={editedCard ? editedCard.assigned_person : ""}
                onChange={handleInputChange}
              />
              <br></br>
              <br></br>
              <TextField
                label="Card End Date"
                variant="outlined"
                name="card_end_date"
                value={editedCard ? editedCard.card_end_date : ""}
                onChange={handleInputChange}
              />
              <br></br>
              <Typography>Card ID: {selectedCard.id}</Typography>
              <br></br>
              <Button
                variant="contained"
                color="primary"
                onClick={handleSubmit}
              >
                Save Changes
              </Button>
              <br></br>
              <br></br>
              <Button
                variant="contained"
                color="secondary"
                onClick={handleDelete}
              >
                Delete Card
              </Button>
              <br></br>
              <br></br>
              <Button
                variant="contained"
                onClick={closeCardModal}
              >
                Close
              </Button>
            </div>
          )}
        </Box>
      </Modal>
    </div>
  );
};

export default Kanbancard2;
