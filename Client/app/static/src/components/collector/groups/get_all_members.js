/**
 * Created by vlad on 16.11.16.
 */

var React = require('react');
import {send_task} from '../../../api/task'
import FormGroup from 'react-bootstrap/lib/FormGroup';
import FormControl from 'react-bootstrap/lib/FormControl';
import ControlLabel from 'react-bootstrap/lib/ControlLabel';
import Button from 'react-bootstrap/lib/Button';

class GetAllMembers extends React.Component{
    method_name='Collector.Groups.get_all_members';
    default_state = {
        group_ids: '',
        limit: 3
    };

    constructor(props) {
        super(props);
        this.state = this.default_state;

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleLimitChange = this.handleLimitChange.bind(this);
    }

    handleChange(event) {
        this.setState({group_ids: event.target.value});
    }

    handleLimitChange(event) {
        this.setState({limit: event.target.value});
    }

    handleSubmit(event) {
        var group_ids = this.state.group_ids.split(',');
        if(this.state.group_ids.length == 0){
            alert('Error!')
        }
        else {
            send_task(this.method_name, {
                'group_ids': group_ids,
                'limit': this.state.limit
            });
        }
        this.setState(this.default_state);
        event.preventDefault();
    }


    render(){
        return(
            <div class = 'content'>
                <div className="page-header">
                    <h1>Сбор подписчиков сообществ</h1>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <FormGroup
                        controlId="formBasicText"
                    >
                        <ControlLabel>Введите список сообществ через запятую:</ControlLabel>
                        <FormControl
                            type="text"
                            value={this.state.group_ids}
                            placeholder="coffman, club1, 2"
                            onChange={this.handleChange}
                        />
                        <ControlLabel>В каком кол-ве сообществ пользователь должен состоять:</ControlLabel>
                        <FormControl
                            type="number"
                            value={this.state.limit}
                            placeholder="3"
                            onChange={this.handleLimitChange}
                        />
                    </FormGroup>
                    <Button type="submit">
                        Отправить
                    </Button>
                </form>
            </div>
        );
    }
};

export default GetAllMembers
