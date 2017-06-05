/**
 * Created by vlad on 21.11.16.
 */

/**
 * Created by vlad on 21.11.16.
 */

var React = require('react');
import {send_task} from '../../../api/task'
import FormGroup from 'react-bootstrap/lib/FormGroup';
import FormControl from 'react-bootstrap/lib/FormControl';
import ControlLabel from 'react-bootstrap/lib/ControlLabel';
import Button from 'react-bootstrap/lib/Button';


class GetMembersRelatives extends React.Component{
    method_name = 'Collector.Groups.get_members_relatives';
    default_state = {group_id: '', value:'sibling'};

    constructor(props) {
        super(props);
        this.state = this.default_state;
        this.handleChange = this.handleChange.bind(this);
        this.handleValueChange = this.handleValueChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({group_id: event.target.value});
    }

    handleValueChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        if(this.state.group_id.length == 0){
            alert('Error!')
        }
        else {
            send_task(this.method_name, {
                'group_id': this.state.group_id,
                'relative_type': this.state.value
            });
        }
        this.setState(this.default_state);
        event.preventDefault();
    }

    render(){
        return(
            <div class = 'content'>
                <div className="page-header">
                    <h1>Сбор родственников подписчиков</h1>
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
                    </FormGroup>
                    <FormGroup controlId="formControlsSelect">
                        <ControlLabel>Выберите тип родственной связи:</ControlLabel>
                        <FormControl componentClass="select" placeholder="select" value={this.state.value} onChange={this.handleValueChange}>
                            <option value="child">сын/дочь</option>
                            <option value="sibling">брат/сестра</option>
                            <option value="parent">отец/мать</option>
                            <option value="grandparent">дедушка/бабушка</option>
                            <option value="grandchild">внук/внучка</option>
                        </FormControl>
                    </FormGroup>
                    <Button type="submit">
                        Отправить
                    </Button>
                </form>
            </div>
        );
    }
};

export default GetMembersRelatives


