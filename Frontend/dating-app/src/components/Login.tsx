import { TextField, Button, Container, Paper, Avatar, Typography, Box, Link } from "@mui/material"
import LockOutlinedIcon from "@mui/icons-material/LockOutlined"
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const LoginPage = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");


    const login = async (username: string, password: string) => {
        return await fetch('https://localhost:8000/auth/login',
            {
                method: "POST",
                body: new URLSearchParams({
                    grant_type: 'password',
                    username: username,
                    password: password,
                    client_id: 'your-client-id',
                    client_secret: 'your-client-secret',
                }),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            }
        ).then((response) => {
            if (response.status === 401) {
                alert("Error. Wrong Credentials");
            }
            else {
                alert("Login successful");
            }

        })


    };

    return (
        <Container sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            minHeight: '100vh',
            // px: -5

        }}>
            <Paper elevation={10} sx={{ padding: 2, width: '100%', maxWidth: 300, marginTop: 8,  }}>
                <Avatar
                    sx={{
                        mx: 'auto',
                        bgcolor: 'primary.main',
                        textAlign: 'center',
                        my: 2,
                        width: 40,

                    }}>

                    <LockOutlinedIcon />
                </Avatar>


                <Typography component="h1" variant="h5" sx={{ textAlign: 'center', mb: 2 }}>
                    Sign In
                </Typography>
                <Box
                component="form"
                onSubmit={(e) => { e.preventDefault(); login(username, password); }}
                 sx={{
                    my: 5
                }}

                >
                    <TextField
                        placeholder="Enter username"
                        fullWidth
                        required
                        autoFocus
                        sx={{ mb: 2 }}
                        value={username}
                        onChange={(e) => setUsername(e.target.value)} />

                    <TextField
                        placeholder="Enter password"
                        fullWidth
                        required
                        type="password"
                        
                        sx={{ my: 2 }}
                        value={password}
                        onChange={(e) => setPassword(e.target.value)} />
                    <Button onClick={() => login(username, password)} variant='contained' fullWidth sx={{ my: 2 }}>
                        Sign In
                    </Button>
                    <Link href="/register" underline="hover" onClick={(e) => { e.preventDefault(); navigate('/register'); }}>
                        {'No account? Register here!'}
                    </Link>
                </Box>
            </Paper>
        </Container>
    )
}

export default LoginPage;