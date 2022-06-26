import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import React from "react";
import Header from "../../components/Header/Header";
import GalleryVP from "../../components/Gallary/VP/GalleryVP";




function GalleryPageVP(props){
    document.title=process.env.REACT_APP_VP
    const host=process.env.REACT_APP_HOST_NAME
    return(
        <Box sx={{ fontFamily: 'Roboto', height: 'auto'}}>

            <Header/>
            <Container sx={{fontFamily: 'Roboto', mt: '20px', justifyContent: 'center'}}>
                <GalleryVP
                    contestName={process.env.REACT_APP_VP}
                    urlVerticalTabs={`${host}/frontend/api/archive/contest/years/`}
                    urlHorizontalTabs={`${host}/frontend/api/archive/contest/nominations/`}
                    urlContent={`${host}/frontend/api/archive/`}>

                </GalleryVP>

            </Container>
        </Box>

    )
}

export default GalleryPageVP