import Card from "@mui/material/Card";
import {CardMedia, Chip} from "@mui/material";
import Box from "@mui/material/Box";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import FieldTitle from "../Gallary/FieldTitle";
import React from "react";
import EventNoteIcon from "@mui/icons-material/EventNote";
import LocationCityIcon from '@mui/icons-material/LocationCity';
import {ButtonDefault} from "../styled";


function CardExposition() {
    return (

        <Card
            sx={{display: 'flex', flexGrow: 1, marginTop: '20px',width:[350,540,540]}}>
            <CardMedia
                component="img"
                sx={{
                     width: [350, 200],
                        display:  'block',
                        justifyContent: 'center',
                        marginLeft: 'auto',


                }}
                image={'http://shkola-nemenskogo.ru/assets/cache_image/expositions/%20%D0%9F%D0%B5%D1%82%D1%80%D0%B0%20%D1%82%D0%B2%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D1%8F_300x0_17c.jpg'}
                alt=''
            />

            <Box sx={{
                display: 'flex',
                // flexWrap: "wrap",
                flexGrow: 1,
                // width: 320
            }}>

                <CardContent sx={{width: [300, 300, 300], display:['none','block','block']}}>
                    <Typography variant="body1" display="block" gutterBottom >
                        Вебинар «Подготовка к участию в Городской
                        научно-практической конференции «АРТвектор»
                    </Typography>
                    <Box component={'div'} sx={{marginTop: '15px'}}>
                        <Chip icon={<EventNoteIcon
                            sx={{color: 'rgb(128,110,110)'}}/>}
                              label="с 15 сентября 2022 г. по  15 октября 2022 г."
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
                        <ButtonDefault variant="outlined" size='small' sx={{marginTop:'30px'}}>
                            Подробнее
                        </ButtonDefault>
                    </Box>


                </CardContent>
            </Box>



        </Card>
    )
}


export default CardExposition