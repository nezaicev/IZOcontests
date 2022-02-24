import React from "react";
import Header from "../components/Header";

import Box from "@material-ui/core/Box";

import PlayerModal from "./PlayerModal";
import {images} from "../data/images";
import ImageGallery from "./ImageGallery";
import Container from "@material-ui/core/Container";
import VideoGallery from "./VideoGallery";

import orange from "@material-ui/core/colors/orange";
import green from "@material-ui/core/colors/green";

import Checkbox from "@material-ui/core/Checkbox";
import {createTheme, ThemeProvider, styled} from '@mui/material/styles';
import Button from "@material-ui/core/Button";
import GlobalTest from "./Test";
import purple from "@material-ui/core/colors/purple";

const ColorButton = styled(Button)(({theme}) => ({
    color: theme.palette.getContrastText(purple[500]),
    backgroundColor: purple[500],
    '&:hover': {
        backgroundColor: purple[700],
    },
}));

const App = () => {

    return (


        <Box sx={{bgcolor: '#f9f8ed', height: '100vh', fontFamily: 'Roboto'}}>
            <Header/>


            <Container sx={{fontFamily: 'Roboto', mt: '20px',justifyContent: 'center'}}>
                <VideoGallery/>
                {/*<ImageGallery images={images}/>*/}


            </Container>


        </Box>


    );

}

export default App;

