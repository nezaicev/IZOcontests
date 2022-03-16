import Box from "@material-ui/core/Box";
import Header from "../components/Header";
import Container from "@material-ui/core/Container";
import MixGallery from "../components/MixGallery";
import React from "react";


function VP(props){
    console.log(process.env.REACT_APP_HOST_NAME)

    return(
        <Box sx={{bgcolor: 'rgb(239 236 227)', fontFamily: 'Roboto', height: 'auto'}}>
            <Header/>
            <Container sx={{fontFamily: 'Roboto', mt: '20px', justifyContent: 'center'}}>
                <MixGallery/>
            </Container>
        </Box>

    )
 }

 export default VP