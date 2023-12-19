import React, { useState } from 'react';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import LogoImg from '../logo.svg';
import Container from '@mui/material/Container';

const SignIn = () => {
  const [loading, setLoading] = useState(false);
  const [isLogin, setIsLogin] = useState(true);
  const [form, setForm] = useState({
    email: '',
    password: '',
  });

    const SignInText = isLogin
    ? "Do not have an account yet?"
    : "Already have an account?";

  const handleChange = (event) => {
    setForm((oldForm) => ({
      ...oldForm,
      [event.target.name]: event.target.value,
    }));
  };

  const handleSignIn = async () => {
    // Implementiere hier deine Anmeldefunktion
  };

  return (
    <Container
      maxWidth="sm"
      sx={{
        mt: 4,
      }}
    >
      <Stack mb={4} spacing={4} alignItems="center" textAlign="center">
        <img 
        src={LogoImg} 
        alt="Brello" 
        style={{ width: '100px', height: 'auto' }}/>
        <Typography color="primary">
          Welcome to Brello
          <br />
          Manage your team's projects from anywhere at any time.
        </Typography>
      </Stack>
      <Stack spacing={2}>
        <TextField
          value={form.email}
          name="email"
          onChange={handleChange}
          label="Email"
        />
        <TextField
          value={form.password}
          type="password"
          name="password"
          onChange={handleChange}
          label="Password"
        />
        <Button
          disabled={!form.email.trim() || !form.password.trim()}
          onClick={handleSignIn}
          size="large"
          variant="contained"
        >
          {isLogin ? "Login" : "Register"} 
        </Button>
      </Stack>
      <Typography
        sx={{
          cursor: "pointer",
          color: "black",  
        }}
        onClick={() => setIsLogin((o) => !o)}
        mt={2}
        textAlign="center"
      >
        {SignInText}
      </Typography>
    </Container>
  );
};

export default SignIn;
