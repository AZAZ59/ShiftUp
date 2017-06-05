/**
 * Created by vlad on 21.11.16.
 */

var React = require('react');
import {send_task} from '../../../api/task'
import FormGroup from 'react-bootstrap/lib/FormGroup';
import FormControl from 'react-bootstrap/lib/FormControl';
import ControlLabel from 'react-bootstrap/lib/ControlLabel';
import Button from 'react-bootstrap/lib/Button';


class GetGroupsPosts extends React.Component{
    method_name = 'Collector.Groups.get_members_groups';
    default_state = {group_id: '', limit: ''};

    constructor(props) {
        super(props);
        this.state = this.default_state;
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleCountChange = this.handleCountChange.bind(this);
    }

    handleChange(event) {
        this.setState({group_id: event.target.value});
    }

    handleCountChange(event) {
        this.setState({limit: event.target.value});
    }


    handleSubmit(event) {
        if(this.state.group_id.length == 0){
            alert('Error!')
        }
        else {
            send_task(this.method_name, {
                'group_id': this.state.group_id,
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
                    <h1>Сбор групп подписчиков</h1>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <FormGroup
                        controlId="formBasicText"
                    >
                        <ControlLabel>Введите ссылку на сообщество:</ControlLabel>
                        <FormControl
                            type="text"
                            value={this.state.group_id}
                            placeholder="coffman"
                            onChange={this.handleChange}
                        />
                        <ControlLabel>Размер минимального пересечения аудитории:</ControlLabel>
                        <FormControl
                            type="number"
                            value={this.state.limit}
                            placeholder="1"
                            onChange={this.handleCountChange}
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

export default GetGroupsPosts

