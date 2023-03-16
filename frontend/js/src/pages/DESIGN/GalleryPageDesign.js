import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import React from "react";
import Header from "../../components/Header/Header";
import useAuth from "../../components/hooks/useAuth";
import GalleryDesign from "../../components/Gallary/Design/GalleryDesign";


function GalleryPageDesign(props) {
    const auth = useAuth()
    document.title = process.env.REACT_APP_DESIGN
    const host = process.env.REACT_APP_HOST_NAME
    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>

            <Header
                auth={auth}
            />
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center'
            }}>
                <GalleryDesign
                    contestName={process.env.REACT_APP_DESIGN}
                    urlVerticalTabs={`${host}/frontend/api/archive/contest/years/`}
                    urlHorizontalTabs={`${host}/frontend/api/archive/contest/nominations/`}
                    urlContent={`${host}/frontend/api/archive/`}>

                </GalleryDesign>

            </Container>
        </Box>

    )
}

export default GalleryPageDesign