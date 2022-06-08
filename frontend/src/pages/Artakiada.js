import Box from "@mui/material/Box";
import Header from "../components/Header";
import Container from "@mui/material/Container";
import VPGallery from "../components/VPGallery";
import React from "react";
import ImageGalleryFetch from "../components/ImageGalleryFetch";


function Artakiada(props) {

    document.title = 'АРТакиада «Изображение и слово»'
    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>
            <Header/>
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center'
            }}>
                <ImageGalleryFetch
                    contestName={process.env.REACT_APP_ARTAKIADA}
                    urlTheme={`http://${process.env.REACT_APP_HOST_NAME}/frontend/api/archive/theme/artakiada`}
                />
            </Container>
        </Box>

    )
}

export default Artakiada