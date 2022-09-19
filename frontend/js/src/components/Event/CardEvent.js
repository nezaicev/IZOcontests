import Card from "@mui/material/Card";
import {CardMedia, Chip} from "@mui/material";
import Box from "@mui/material/Box";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import FieldTitle from "../Gallary/FieldTitle";
import React from "react";
import EventNoteIcon from '@mui/icons-material/EventNote';
import Button from "@mui/material/Button";
import {brown } from '@mui/material/colors';
import {ButtonDefault} from "../styled";

const buttonColor=brown.A400

function CardEvent() {
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
                image={'http://cnho.ru/art-teach/kult_nasled_2022-23/gelikon.png'}
                alt=''
            />

            <Box sx={{
                flexWrap: "wrap",
                flexGrow: 1,
                width: 200
            }}>

                <CardContent sx={{width: [300, 300, 300]}}>
                    <Typography variant="body1" display="block" gutterBottom>
                        Вебинар «Подготовка к участию в Городской
                        научно-практической конференции «АРТвектор»
                    </Typography>
                    <Box component={'div'} sx={{marginTop: '15px'}}>
                        <Chip icon={<EventNoteIcon
                            sx={{color: 'rgb(128,110,110)'}}/>}
                              label="15 сентября 2022 г. 16:00"
                              variant="outlined"/>
                    </Box>




                    <Typography variant="subtitle1" color="text.secondary"
                                component="div"
                                sx={{
                                    alignContent: 'center',
                                    display: 'block',
                                    marginTop: '15px'
                                }}>
                        Контент

                    </Typography>
                    <Box componetn={'div'} sx={{
                        justifyContent: 'right',
                        display: 'flex'
                    }}>
                        <ButtonDefault variant="outlined"  size='small'>
                            Принять участие
                        </ButtonDefault>
                    </Box>


                </CardContent>
            </Box>



        </Card>
    )
}


export default CardEvent