
import React, {useEffect, useState} from "react";
import {Box} from "@mui/material";
import dataFetch from "../../components/utils/dataFetch";
import {getExcludeData} from "../../components/utils/utils";
import HorizontalTabs from "../../components/Gallary/HorizontalTabs";
import VerticalTabs from "../../components/Gallary/VerticalTabs";
import VisibleBoxImages from "../../components/Gallary/VisibleBoxImages";

const excludeYears = ['2023-2024 год']
const contestName=process.env.REACT_APP_ART_CHALLENGE

// document.title=contestName

function ArtChallengeListPage(props) {
    const [dataVerticalTabs, setDataVerticalTabs] = React.useState([])
    const [valueVerticalTabs, setValueVerticalTabs] = React.useState('')
    const [dataHorizontalTabs, setDataHorizontalTabs] = React.useState([])
    const [valueHorizontalTabs, setValueHorizontalTabs] = React.useState(0)
    // const [valueCreativeTack, setValueCreativeTack] = React.useState('')
    const [params, setParams] = React.useState({contest_name: contestName })
    const [page, setPage] = useState(1)


    useEffect(() => {
        dataFetch(props.urlVerticalTabs, params, (data) => {
            setDataVerticalTabs(getExcludeData(data, excludeYears), [setValueVerticalTabs(0)]);
        })
    }, [])

    useEffect(() => {

        params['year_contest'] = dataVerticalTabs[valueVerticalTabs]
        if (params['year_contest']){
        dataFetch(props.urlHorizontalTabs, params, (data) => {
            setDataHorizontalTabs(data, [setValueHorizontalTabs(0)])
            setPage(1)
        })}
    }, [valueVerticalTabs])

    useEffect(() => {
        params['year_contest'] = dataVerticalTabs[valueVerticalTabs]
        params['theme'] = dataHorizontalTabs[valueHorizontalTabs]
        // dataFetch(props.urlCreativeTack, params, (data) => {
        //     setValueCreativeTack(data)
        // })
    }, [dataHorizontalTabs, valueHorizontalTabs])

    return (<React.Fragment>
            <Box sx={{
                display: 'flex',
                flexWrap: 'wrap',
                justifyContent: 'center',
                alignItems: 'center'
            }}>

                <HorizontalTabs contestName={contestName}
                                data={dataHorizontalTabs}
                                setValueHorizontalTabs={(newValue) => (setValueHorizontalTabs((newValue), [setPage(1)]))}
                                valueVerticalTabs={valueVerticalTabs}
                />

                <VerticalTabs contestName={contestName}
                              data={dataVerticalTabs}
                              setValueVerticalTabs={(newValue) => (setValueVerticalTabs(newValue, [setPage(1)]))}

                />
            </Box>

            {/*<CreativeTack data={valueCreativeTack}/>*/}

            <Box sx={{}}>

                <VisibleBoxImages
                    url={props.urlContent}
                    contestName={contestName}
                    year={dataVerticalTabs[valueVerticalTabs]}
                    theme={dataHorizontalTabs[valueHorizontalTabs]}
                    page={page}
                    ordering={'rating'}
                    setPage={(newValue) => {
                        setPage(newValue)
                    }}
                />

            </Box>
        </React.Fragment>
    )
}

export {ArtChallengeListPage}