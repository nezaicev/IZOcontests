import React, {useEffect, useState} from "react";
import {CircularProgress, Grid} from "@mui/material";
import CardExposition from "../../components/Exposition/CardExposition";
import Box from "@mui/material/Box";
import dataFetch from "../../components/utils/dataFetch";
import {useSearchParams} from "react-router-dom";
import {years_expositions} from "../../components/utils/utils"
import HorizontalTabs from "../../components/Gallary/HorizontalTabs";

const Archive = (props) => {
    const [searchParams] = useSearchParams();
    const [years, setYears] = React.useState([]);
    const [valueHorizontalTabs, setValueHorizontalTabs] = React.useState(0)
    const apiLink = '/frontend/api/exposition_list'
    const [data, setData] = React.useState([])
    const [fetchAll, setFetchAll] = useState(false);

    useEffect(() => {
        dataFetch(`${process.env.REACT_APP_HOST_NAME}/frontend/api/expositions_years/`, {}, (data) => {
            setYears(data)
        })

    }, [])

    useEffect(() => {
        setData([])
        setFetchAll(false)
        if (years.length > 0) {
            dataFetch(`${process.env.REACT_APP_HOST_NAME}${apiLink}`, {
                year: years[valueHorizontalTabs],
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
            marginBottom:'10px'
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
                                  sx={{justifyContent: data.length > 2 ? 'space-between' : 'flex-start'}}>
                                {data.map((item, index) => (

                                    <Grid item xs="auto"
                                          key={index}>
                                        <CardExposition
                                            data={item}/>
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