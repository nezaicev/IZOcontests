import Box from "@mui/material/Box";
import Header from "../components/Header";
import Container from "@mui/material/Container";
import VPGallery from "../components/VPGallery";
import React from "react";


function VP(props){

    document.title='Выставочные проекты'
    return(
        <Box sx={{ fontFamily: 'Roboto', height: 'auto'}}>
            <Header/>
            <Container sx={{fontFamily: 'Roboto', mt: '20px', justifyContent: 'center'}}>
                <VPGallery contestName={process.env.REACT_APP_VP}/>
            </Container>
        </Box>

    )
 }

 export default VP