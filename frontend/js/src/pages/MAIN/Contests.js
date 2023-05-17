import React, {useEffect, useState} from "react";
import Header from "../../components/Header/Header";
import Box from "@mui/material/Box";
import {CircularProgress, Grid} from "@mui/material";
import CardContest from "../../components/Contest/CardContest";
import {useOutletContext} from "react-router-dom";
import dataFetch from "../../components/utils/dataFetch";
import Button from "@mui/material/Button";


const Contests = () => {
    const apiLink='/frontend/api/contests/'

    const [fetchAll, setFetchAll] = useState(false);
    const [data, setData] = React.useState([])
    const auth = useOutletContext()

    useEffect(() => {
        dataFetch(`${process.env.REACT_APP_HOST_NAME}${apiLink}`, null, (data) => {
            setData(data)
            setFetchAll(true)
        })

    }, [])
    return (
        <>

            {function () {
                if (fetchAll) {
                    return (
                        <Box sx={{
                            display: 'grid',
                            gridTemplateColumns: `repeat(auto-fill, minmax(320px, 1fr))`,
                            justifyItems: 'center',
                            alignItems: 'stretch',
                            marginBottom: '30px',

                        }}>
                            {data.map((item, index) => (
                            <Grid item xs="auto" sx={{margin: '20px'}}
                                  key={index}>

                                <CardContest
                                    data={item}
                                    auth={auth}
                                />

                            </Grid>
                            ))}
                        </Box>
                    )
                } else {
                    return (
                        <Box sx={{
                            justifyContent: 'center',
                            height: '600',
                            display: 'flex',
                            marginTop: ' 20px'
                        }}>
                            <CircularProgress sx={{
                                color: '#d26666'
                            }}/>
                        </Box>
                    )
                }
            }()

            }
        </>

    )
}

export {Contests}