import React, {Component} from "react";
import { Button, Grid, Typography, TextField, FormHelperText, FormControl, 
    FormControlLabel, RadioGroup, Radio } from "@mui/material";

export default class CreateRoomPage extends Component {
    defaultVotes = 2;
    
    constructor(props){
        super(props);
    }

    render() {
        return (
            <Grid contaniner spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component="h4" variant="h4">
                        Create a room
                    </Typography>
                </Grid>
            </Grid>
        );
    }
}