from flask import Flask, render_template, request

app = Flask(__name__)

# Data structure for AI tools
tools_data = {
    'Khalid': [
        {'name': 'Tool 1', 'description': 'Description of Tool 1'},
        {'name': 'Tool 2', 'description': 'Description of Tool 2'}
    ],
    'Ahmed': [
        {'name': 'Tool 3', 'description': 'Description of Tool 3'},
        {'name': 'Tool 4', 'description': 'Description of Tool 4'}
    ],
    # Add data for other team members here
}

# Navbar and footer data
navbar_data = list(tools_data.keys())
footer_text = '© 2023 Rehan Labs'

@app.route('/')
def index():
    return render_template('index.html', navbar=navbar_data, footer=footer_text)

@app.route('/<member>')
def team_member_page(member):
    if member in tools_data:
        return render_template('team_member.html', team_member=member, tools_data=tools_data, navbar=navbar_data, footer=footer_text)
    else:
        return "Team member not found."

@app.route('/search', methods=['POST'])
def search_tools():
    search_query = request.form.get('search_query').lower()
    results = {}

    for member, tools in tools_data.items():
        matching_tools = [tool for tool in tools if search_query in tool['name'].lower() or search_query in tool['description'].lower()]
        if matching_tools:
            results[member] = matching_tools

    return render_template('search_results.html', search_query=search_query, results=results, navbar=navbar_data, footer=footer_text)

if __name__ == '__main__':
    app.run(debug=True)
