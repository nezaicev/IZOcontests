import Box from "@mui/material/Box";
import Header from "../../components/Header/Header";
import Container from "@mui/material/Container";
import React from "react";
import Typography from "@mui/material/Typography";
import {useParams} from "react-router-dom";


function EventPage(props) {

    let { id } = useParams();
    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>
            <Header/>
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center'
            }}>
                <Box sx={{display:'flex'}}>
                      <Typography variant="body1" display="block" gutterBottom>
                        Вебинар «Подготовка к участию в Городской
                        научно-практической конференции «АРТвектор»
                          <h3>{id}</h3>
                    </Typography>

                </Box>

            </Container>
        </Box>

    )
}

export default EventPage