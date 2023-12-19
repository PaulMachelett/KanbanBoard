import React, { useState, useEffect } from "react";
import { Stack, Grid, Typography, Box, Paper, Container } from "@mui/material";
import IconButton from "@mui/material/IconButton";
import PersonAddAltIcon from "@mui/icons-material/PersonAddAlt";
import TuneIcon from "@mui/icons-material/Tune";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";

const Projectview = ({ project: initialProject }) => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    setProjects(initialProject);
  }, [initialProject]);

  const handleAddProject = () => {
    console.log("Add Project Clicked!");
  };

  return (
    <Container
      sx={{
        flexDirection: "column",
      }}
    >
      {projects.map((projectinfos) => (
        <Paper
          elevation={3}
          style={{ marginBottom: "20px", padding: "15px" }}
          key={projectinfos.id}
        >
          <Container>
            <h6 variant="h6" color="white">
              Project Name: {projectinfos.name}
            </h6>
            <h6 variant="caption" color="white">
              Created at: {projectinfos.start_date}
            </h6>
            <h6 variant="caption" color="white">
              End Date: {projectinfos.end_date}
            </h6>
          </Container>

          <Stack
            direction="row"
            spacing={2}
            sx={{ justifyContent: "center", paddingRight: 2, marginTop: 2 }}
          >
            <IconButton color="white" aria-label="Settings" mt={2}>
              <TuneIcon />
            </IconButton>
            <IconButton color="white" aria-label="Assign Person" mt={2}>
              <PersonAddAltIcon />
            </IconButton>
          </Stack>

          <IconButton onClick={handleAddProject}>
            <AddCircleOutlineIcon />
          </IconButton>
        </Paper>
      ))}
    </Container>
  );
};

export default Projectview;
