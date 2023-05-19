import React, {useEffect, useState} from "react";
import {CircularProgress, Grid} from "@mui/material";
import Box from "@mui/material/Box";
import dataFetch from "../../components/utils/dataFetch";
import {useSearchParams} from "react-router-dom";
import HorizontalTabs from "../../components/Gallary/HorizontalTabs";
import {lazy, Suspense} from 'react';

const CardExposition = lazy(() => import('../../components/Exposition/CardExposition'));


const Archive = (props) => {
    const [searchParams, setSearchParams] = useSearchParams();
    const [years, setYears] = React.useState([]);
    const [valueHorizontalTabs, setValueHorizontalTabs] = React.useState(0)
    const apiLink = '/frontend/api/exposition_list'
    const [data, setData] = React.useState([])
    const [fetchAll, setFetchAll] = useState(false);

    useEffect(() => {
        dataFetch(`${process.env.REACT_APP_HOST_NAME}/frontend/api/expositions_years/`, {is_archive:1}, (data) => {
            setYears(data)
        })

    }, [])

    useEffect(() => {
        setData([])
        setFetchAll(false)

        if (years.length > 0) {
            searchParams.set('year', years[valueHorizontalTabs]);
            setSearchParams(searchParams)
            dataFetch(`${process.env.REACT_APP_HOST_NAME}${apiLink}`, {
                year: searchParams.get('year') ? searchParams.get('year') : years[valueHorizontalTabs],
                is_archive: props.isArchive
            }, (data) => {
                setData(data)
                setFetchAll(true)
            })
        }
    }, [years, valueHorizontalTabs])


    return (
        <> <Box sx={{
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'center',
            alignItems: 'center',
            marginBottom: '10px'
        }}>
            <HorizontalTabs contestName={props.contestName}
                            data={years}
                            setValueHorizontalTabs={(newValue) => (setValueHorizontalTabs((newValue)))}
            />
        </Box>
            {function () {

                if (fetchAll
                    || data.length > 0) {
                    return (
                        <Box sx={{display: 'flex'}}>
                            <Grid container spacing={2}
                                  sx={{justifyContent: data.length > 2 ? 'center' : 'flex-start'}}>
                                {data.map((item, index) => (

                                    <Grid item xs="auto" sx={{margin:'15px'}}
                                          key={index}>
                                        <Suspense fallback={<div>Загрузка...</div>}>
                                            <CardExposition
                                                data={item}/>
                                        </Suspense>
                                    </Grid>

                                ))}
                            </Grid>
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

            }()}


        </>
    )
}


export {Archive}