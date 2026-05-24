import Box from "@mui/material/Box";
import {CircularProgress, Grid, Paper, Typography, Avatar} from "@mui/material";
import React, {useEffect, useState} from "react";
import {host} from "../../components/utils/consts";
import {useParams, useNavigate} from "react-router-dom";
import dataFetch from "../../components/utils/dataFetch";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import {CardActionArea} from "@mui/material";
import LocationOnIcon from "@mui/icons-material/LocationOn";


function ExpositionURAO(props) {
    const [fetchAll, setFetchAll] = useState(false);
    const [profiles, setProfiles] = React.useState([])
    const navigate = useNavigate();
    let {id} = useParams()

    useEffect(() => {
        dataFetch(`${host}/urao/api/profiles/`, null, (data) => {
            const profilesData = Array.isArray(data) ? data : (data.results || []);
            setProfiles(profilesData);
            setFetchAll(true)
        })
    }, [])


    return (<>
        <Box>
            {fetchAll ? <Box>
                {props.expositionData && (
                    <>
                        <Box sx={{
                            justifyContent: 'center',
                            display: 'flex',
                            marginTop: '15px',
                            marginBottom: '15px'
                        }}>
                            <Typography variant="h5">
                                {props.expositionData.title}
                            </Typography>
                        </Box>

                        {props.expositionData.address && (<Box sx={{
                            display: 'flex'
                        }}>
                            <LocationOnIcon
                                sx={{color: 'rgb(128,110,110)'}}/>
                            <Typography sx={{fontSize: [10, 12, 14]}} variant="overline" display="block"
                                        gutterBottom>
                                {props.expositionData.address}
                            </Typography>
                        </Box>)}


                        {props.expositionData.content && (
                            <Paper
                                dangerouslySetInnerHTML={{__html: props.expositionData.content}}
                                scroll={'body'}
                                sx={{
                                    boxShadow: 0,
                                    maxHeight: 600,
                                    overflow: 'auto',
                                    padding: ['5px', '15px'],
                                    marginBottom: '20px'
                                }}
                            />
                        )}
                    </>
                )}

                {!props.expositionData && (
                    <Box sx={{
                        justifyContent: 'center',
                        display: 'flex',
                        marginTop: '15px',
                        marginBottom: '15px'
                    }}>
                        <Typography variant="h5">
                            Выпускники УРАО
                        </Typography>
                    </Box>
                )}

                <Box sx={{display: 'flex', justifyContent: 'center', marginBottom: '100px'}}>
                    <Grid container spacing={3}
                          sx={{justifyContent: 'center', maxWidth: '1200px'}}>
                        {profiles.map((profile, index) => (
                            <Grid item xs={12} sm={6} md={4} key={index}>
                                <Card sx={{
                                    // height: '80%%',
                                    display: 'flex',
                                    flexDirection: 'column'
                                }}>
                                    <CardActionArea
                                        onClick={() => {
                                            navigate(`/urao/profile/${profile.id}/`);
                                        }}
                                    >
                                        <Box sx={{
                                            display: 'flex',
                                            justifyContent: 'center',
                                            padding: '20px'
                                        }}>
                                            <Avatar
                                                src={profile.avatar_thumb}
                                                alt={profile.full_name}
                                                sx={{width: 150, height: 150}}
                                            />
                                        </Box>
                                        <CardContent>
                                            <Typography gutterBottom variant="h6" component="div"
                                                        sx={{
                                                            textAlign: 'center',
                                                            fontSize: {xs: '0.7rem', sm: '0.9rem', md: '1rem'}
                                                        }}>
                                                {profile.full_name}
                                            </Typography>
                                            {profile.year_graduation && (
                                                <Typography variant="body2" color="text.secondary"
                                                            sx={{textAlign: 'center'}}>
                                                    Год выпуска: {profile.year_graduation}
                                                </Typography>
                                            )}
                                            <Typography variant="body2" color="text.secondary"
                                                        sx={{textAlign: 'center', marginTop: '5px'}}>
                                                Работ: {profile.works_count}
                                            </Typography>
                                        </CardContent>
                                    </CardActionArea>
                                </Card>
                            </Grid>
                        ))}
                    </Grid>
                </Box>

            </Box> : <Box sx={{
                justifyContent: 'center',
                height: '600',
                display: 'flex',
                marginTop: ' 20px'
            }}>
                <CircularProgress sx={{
                    color: '#d26666'
                }}/>
            </Box>
            }

        </Box>


    </>)
}


export {ExpositionURAO}