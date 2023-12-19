import React from 'react';
import { Button, Stack, AppBar, Toolbar, Typography } from '@mui/material';
import LogoutIcon from '@mui/icons-material/Logout';
import LogoImg from '../logo.svg';

const Topbar = () => {
  return (
    <AppBar position="static">
    <Toolbar
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
      <Stack direction="row" alignItems="center" spacing={2} sx={{ marginLeft: '10px' }}></Stack>
        <img src={LogoImg} alt="Brello Logo" style={{ height: '30px', marginRight: '10px' }} />
        <Typography variant="h6" component="div">
          Brello
        </Typography>
        <Stack direction="row" spacing={2}>
          <Button variant="contained">Create a board</Button>
          <Button color="inherit" startIcon={<LogoutIcon />}>
            Logout
          </Button>
        </Stack>
      </Toolbar>
    </AppBar>
  );
};

export default Topbar;

