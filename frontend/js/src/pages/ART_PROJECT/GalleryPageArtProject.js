import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import React from "react";
import Header from "../../components/Header/Header";
import GalleryVP from "../../components/Gallary/VP/GalleryVP";
import useAuth from "../../components/hooks/useAuth";


function GalleryPageArtProject(props) {

    document.title = process.env.REACT_APP_ART_PROJECT
    const host = process.env.REACT_APP_HOST_NAME
    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>


            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center'
            }}>
                <GalleryVP
                    contestName={process.env.REACT_APP_ART_PROJECT}
                    urlVerticalTabs={`${host}/frontend/api/archive/contest/years/`}
                    urlHorizontalTabs={`${host}/frontend/api/archive/contest/nominations/`}
                    urlContent={`${host}/frontend/api/archive/`}
                >

                </GalleryVP>

            </Container>
        </Box>

    )
}

export default GalleryPageArtProject