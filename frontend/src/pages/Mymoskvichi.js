import Box from "@material-ui/core/Box";
import Header from "../components/Header";
import Container from "@material-ui/core/Container";
import MixGallery from "../components/MixGallery";
import React from "react";


function Mymoskvichi(props){

    document.title='КОНКУРС МУЛЬТИМЕДИА «МЫ МОСКВИЧИ»'
    return(
        <Box sx={{ fontFamily: 'Roboto', height: 'auto'}}>
            <Header/>
            <Container sx={{fontFamily: 'Roboto', mt: '20px', justifyContent: 'center'}}>
                <MixGallery contestName={process.env.REACT_APP_VP}/>
            </Container>
        </Box>

    )
 }

 export default Mymoskvichi