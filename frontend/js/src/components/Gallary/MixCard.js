
import  Card,{ cardClasses} from "@mui/material/Card";
import {styled} from "@mui/material/styles";

 const MixCard = styled(Card)(() => ({
    justifyContent: 'center',
    alignItems: 'baseline',
    flexDirection: 'column',
    margin: '20px',
    marginTop: '30px',
    padding: '20px',
    height: 'fit-content',

}))

export default MixCard

