import Box from "@material-ui/core/Box";
import Header from "../components/Header";
import Container from "@material-ui/core/Container";
import MixGallery from "../components/MixGallery";
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