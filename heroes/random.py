import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class NetflixAnalyticsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Netflix Data Analytics App")

        # Load sample Netflix dataset
        self.df = pd.read_csv(".csv")  # Replace with your dataset

        # Create and set up GUI components
        self.create_widgets()

    def create_widgets(self):
        # Label and Dropdown for selecting analysis
        self.label_analysis = tk.Label(self.root, text="Select Analysis:")
        self.label_analysis.pack(pady=10)

        self.analysis_var = tk.StringVar()
        self.analysis_var.set("Select Analysis")
        self.dropdown_analysis = ttk.Combobox(
            self.root, textvariable=self.analysis_var, values=["Genres", "Ratings"]
        )
        self.dropdown_analysis.pack()

        # Button to trigger analysis
        self.btn_analyze = tk.Button(
            self.root, text="Analyze", command=self.analyze_data
        )
        self.btn_analyze.pack(pady=10)

        # Matplotlib canvas for displaying plots
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot_canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.plot_widget = self.plot_canvas.get_tk_widget()
        self.plot_widget.pack()

    def analyze_data(self):
        analysis_type = self.analysis_var.get()

        if analysis_type == "Genres":
            self.plot_genres_distribution()
        elif analysis_type == "Ratings":
            self.plot_ratings_distribution()

    def plot_genres_distribution(self):
        genre_counts = self.df["Genres"].value_counts()
        ax = self.figure.add_subplot(111)
        ax.clear()
        genre_counts.plot(kind="bar", ax=ax)
        ax.set_title("Distribution of Genres on Netflix")
        ax.set_xlabel("Genres")
        ax.set_ylabel("Count")
        self.plot_canvas.draw()

    def plot_ratings_distribution(self):
        ratings_counts = self.df["Ratings"].value_counts()
        ax = self.figure.add_subplot(111)
        ax.clear()
        ratings_counts.plot(kind="bar", ax=ax)
        ax.set_title("Distribution of Ratings on Netflix")
        ax.set_xlabel("Ratings")
        ax.set_ylabel("Count")
        self.plot_canvas.draw()


# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = NetflixAnalyticsApp(root)
    root.mainloop()
