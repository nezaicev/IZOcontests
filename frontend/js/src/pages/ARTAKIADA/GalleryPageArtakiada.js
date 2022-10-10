import Box from "@mui/material/Box";
import Header from "../../components/Header/Header";
import Container from "@mui/material/Container";

import React from "react";
import GalleryArtakiada
    from "../../components/Gallary/Artakiada/GalleryArtakiada";
import useAuth from "../../components/hooks/useAuth";

function GalleryPageArtakiada(props){
    const auth = useAuth()
    document.title=process.env.REACT_APP_ARTAKIADA
    const host=process.env.REACT_APP_HOST_NAME
    return(
        <Box sx={{ fontFamily: 'Roboto', height: 'auto'}}>

            <Header auth={auth}/>
            <Container sx={{fontFamily: 'Roboto', mt: '20px', justifyContent: 'center'}}>
                <GalleryArtakiada
                    contestName={process.env.REACT_APP_ARTAKIADA}
                    urlVerticalTabs={`${host}/frontend/api/archive/contest/years/`}
                    urlHorizontalTabs={`${host}/frontend/api/archive/contest/thems/`}
                    urlCreativeTack={`${host}/frontend/api/contest/creative_tack/`}
                    urlContent={`${host}/frontend/api/archive/`}>

                </GalleryArtakiada>

            </Container>
        </Box>

    )
}

export default GalleryPageArtakiada