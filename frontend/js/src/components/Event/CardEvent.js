import Card from "@mui/material/Card";
import {CardMedia, Chip, Paper} from "@mui/material";
import Box from "@mui/material/Box";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import FieldTitle from "../Gallary/FieldTitle";
import React from "react";
import EventNoteIcon from '@mui/icons-material/EventNote';
import Button from "@mui/material/Button";
import {brown} from '@mui/material/colors';
import {ButtonDefault, DividerStyled} from "../styled";
import {getFormattedDate} from "../utils/utils";

const buttonColor = brown.A400

function CardEvent(props) {
    return (

        <Card
            sx={{
                display: 'flex',
                flexWrap: 'wrap',
                marginTop: '20px',
                width: 350
            }}>
            <CardMedia
                component="img"
                sx={{
                    width: 350,
                    display: 'block',
                }}
                image={props.data['logo']}
                alt=''
            />

            <Box sx={{
                flexWrap: "wrap",
                flexGrow: 1,
                width: 200,
                display: 'flex',
                justifyContent:'center',
            }}>

                <CardContent>
                    <Typography variant="body1" display="block" gutterBottom>
                        {props.data['name']}
                    </Typography>
                    <Box component={'div'} sx={{marginTop: '15px'}}>
                        <Chip icon={<EventNoteIcon
                            sx={{color: 'rgb(128,110,110)'}}/>}
                              label={getFormattedDate(props.data['start_date'])}
                              variant="outlined"/>
                    </Box>

                    <Box component={'div'} sx={{margin:'5px'}}>
                    <Typography variant="subtitle1" color="text.secondary"
                                component="div"
                                sx={{
                                    alignContent: 'center',
                                    display: 'block',
                                    marginTop: '15px'
                                }}

                    >
                        {props.data['message']}

                    </Typography>
                        </Box>
                    <DividerStyled/>
                    <Box componetn={'div'} sx={{
                        justifyContent: 'right',
                        display: 'flex',
                        margin: '5px'
                    }}>
                        <ButtonDefault variant="outlined" size='small'>
                            Принять участие
                        </ButtonDefault>
                    </Box>


                </CardContent>
            </Box>


        </Card>
    )
}


export default CardEvent