import * as React from 'react';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';


export default function SimpleContainer() {
    return (
        <React.Fragment>

            <Container component={'div'} >
                <Box sx={{ bgcolor: '#cfe8fc', height: '100vh' }} />

            </Container>
        </React.Fragment>
    );
}