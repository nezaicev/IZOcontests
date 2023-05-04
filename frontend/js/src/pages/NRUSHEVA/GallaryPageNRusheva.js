import Box from "@mui/material/Box";
import Header from "../../components/Header/Header";
import Container from "@mui/material/Container";

import React from "react";

import GalleryNRusheva
    from "../../components/Gallary/NRusheva/GalleryNRusheva";
import useAuth from "../../components/hooks/useAuth";

function GalleryPageNRusheva(props) {
    const auth = useAuth()
    document.title = process.env.REACT_APP_NRUSHEVA
    const host = process.env.REACT_APP_HOST_NAME
    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>

            <Header auth={auth}/>
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center'
            }}>
                <GalleryNRusheva
                    contestName={process.env.REACT_APP_NRUSHEVA}
                    urlVerticalTabs={`${host}/frontend/api/archive/contest/years/`}
                    urlHorizontalTabs={`${host}/frontend/api/archive/contest/thems/`}
                    urlCreativeTack={`${host}/frontend/api/contest/creative_tack/`}
                    urlContent={`${host}/frontend/api/archive/`}>
                </GalleryNRusheva>

            </Container>
        </Box>

    )
}

export default GalleryPageNRusheva