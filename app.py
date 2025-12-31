from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect root to news or about, or render one of them. 
    # Let's render news as the default home page.
    return news()

@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html', title="Subscribe")

@app.route('/news')
def news():
    # Arbitrary made-up news data
    # Using 'url' key as requested
    weekly_briefs = [
        {
            "title": "Sunrise Tech: The Shift to Solar Servers",
            "date": "Oct 24, 2025",
            "summary": "Major tech giants announce a collective shift to solar-only data centers by 2030.",
            "url": "#"
        },
        {
            "title": "Global Coffee Yields Hit Record High",
            "date": "Oct 23, 2025",
            "summary": "Unexpected rainfall in the equatorial belt leads to a surplus in Arabica beans, lowering prices.",
            "url": "#"
        },
        {
            "title": "Urban Quiet Zones",
            "date": "Oct 22, 2025",
            "summary": "Metropolises like London and New York pilot 'silent hours' for construction to improve mental health.",
            "url": "#"
        }
    ]
    return render_template('news.html', title="Weekly News", news=weekly_briefs)

if __name__ == '__main__':
    app.run(debug=True)