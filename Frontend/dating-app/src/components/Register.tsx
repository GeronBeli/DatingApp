import { TextField, Button, Container, Paper, Avatar, Typography, Box, Link } from "@mui/material"
import LockOutlinedIcon from "@mui/icons-material/LockOutlined"
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const RegisterPage = () => {
    const navigate = useNavigate();
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [username, setUsername] = useState("");
    const [birthday, setBirthday] = useState("");
    const [password, setPassword] = useState("");
    const [repeatPassword, setRepeatPassword] = useState("");

    const register = async () => {
        // Placeholder for registration logic
        console.log({
            firstName,
            lastName,
            username,
            birthday,
            password,
            repeatPassword,
        });
        if (password !== repeatPassword) {
            alert("Passwords do not match!");
            return;
        }
        alert("Registration successful (placeholder)");
    };

    return (
        <Container sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            minHeight: '100vh',
        }}>
            <Paper elevation={10} sx={{ padding: 2, width: '100%', maxWidth: 400, marginTop: 8 }}>
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
                    Sign Up
                </Typography>
                <Box
                    component="form"
                    onSubmit={(e) => { e.preventDefault(); register(); }}
                    sx={{ my: 5 }}
                >
                    <TextField
                        placeholder="Enter first name"
                        fullWidth
                        required
                        autoFocus
                        sx={{ mb: 2 }}
                        value={firstName}
                        onChange={(e) => setFirstName(e.target.value)} />
                    <TextField
                        placeholder="Enter last name"
                        fullWidth
                        required
                        sx={{ mb: 2 }}
                        value={lastName}
                        onChange={(e) => setLastName(e.target.value)} />
                    <TextField
                        placeholder="Enter username"
                        fullWidth
                        required
                        sx={{ mb: 2 }}
                        value={username}
                        onChange={(e) => setUsername(e.target.value)} />
                    <TextField
                        label="Birthday"
                        type="date"
                        fullWidth
                        required
                        sx={{ mb: 2 }}
                        value={birthday}
                        onChange={(e) => setBirthday(e.target.value)}
                        slotProps={{
                            inputLabel: {
                                shrink: true
                            }
                        }}

                    />
                    <TextField
                        placeholder="Enter password"
                        fullWidth
                        required
                        type="password"
                        sx={{ my: 2 }}
                        value={password}
                        onChange={(e) => setPassword(e.target.value)} />
                    
                    <TextField
                        placeholder="Repeat password"
                        fullWidth
                        required
                        type="password"
                        sx={{ my: 2 }}
                        value={repeatPassword}
                        onChange={(e) => setRepeatPassword(e.target.value)} />
                    {repeatPassword && password !== repeatPassword && (
                        <Typography variant="body2" sx={{ color: 'error.main', mt: -1, mb: 2 }}>
                            Passwords do not match
                        </Typography>
                    )}
                    <Button onClick={register} variant='contained' fullWidth sx={{ my: 2 }}>
                        Sign Up
                    </Button>
                    <Link href="/" underline="hover" onClick={(e) => { e.preventDefault(); navigate('/'); }}>
                        {'Already have an account? Sign In'}
                    </Link>
                </Box>
            </Paper>
        </Container>
    )
}

export default RegisterPage;
