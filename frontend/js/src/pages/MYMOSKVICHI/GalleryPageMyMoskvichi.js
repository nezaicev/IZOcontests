import Box from "@mui/material/Box";
import Header from "../../components/Header/Header";
import Container from "@mui/material/Container";

import React from "react";

import GalleryMyMoskvichi
    from "../../components/Gallary/MyMoskvichi/GalleryMyMoskvichi";
import useAuth from "../../components/hooks/useAuth";

function GalleryPageMyMoskvichi(props) {
    const auth = useAuth()
    document.title = process.env.REACT_APP_MYMOSKVICHI
    const host = process.env.REACT_APP_HOST_NAME
    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>

            <Header auth={auth}/>
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center'
            }}>
                <GalleryMyMoskvichi
                    contestName={process.env.REACT_APP_MYMOSKVICHI}
                    urlVerticalTabs={`${host}/frontend/api/archive/contest/years/`}
                    urlHorizontalTabs={`${host}/frontend/api/archive/contest/nominations/`}
                    // urlCreativeTack={`${host}/frontend/api/contest/creative_tack/`}
                    urlContent={`${host}/frontend/api/archive/`}>

                </GalleryMyMoskvichi>

            </Container>
        </Box>

    )
}

export default GalleryPageMyMoskvichi