from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import os

class TaskReportGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=1,  # Center
            textColor=colors.darkblue
        )
        self.heading_style = ParagraphStyle(
            'CustomHeading',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=12,
            textColor=colors.darkgreen
        )
        
    def create_report(self, filename="Shadow_Fox_Internship_Tasks_Report.pdf"):
        doc = SimpleDocTemplate(filename, pagesize=A4)
        story = []
        
        # Title Page
        story.append(Paragraph("Shadow Fox Internship", self.title_style))
        story.append(Paragraph("Complete Tasks Report", self.title_style))
        story.append(Spacer(1, 0.5*inch))
        
        # Report Info
        report_info = [
            ["Report Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            ["Intern Name:", "Sachin Kumar"],
            ["Email:", "sach872266in@gmail.com"],
            ["GitHub Repository:", "https://github.com/sach200/shadow-fox-internship"],
            ["Total Tasks Completed:", "3 Tasks (Beginner + Intermediate + Advanced)"]
        ]
        
        info_table = Table(report_info, colWidths=[2*inch, 4*inch])
        info_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(info_table)
        story.append(PageBreak())
        
        # Task 1: Hangman Game
        story.append(Paragraph("Task 1: Hangman Game (Beginner Level)", self.heading_style))
        story.append(Paragraph("<b>Objective:</b> Create an interactive word-guessing game", self.styles['Normal']))
        story.append(Spacer(1, 12))
        
        hangman_features = [
            ["Feature", "Implementation", "Status"],
            ["Word Selection", "Random word from predefined list", "✓ Complete"],
            ["User Input", "Letter guessing with validation", "✓ Complete"],
            ["Game Logic", "Track guesses, wins, losses", "✓ Complete"],
            ["Visual Display", "ASCII hangman drawing", "✓ Complete"],
            ["Enhanced Version", "Categories, difficulty levels, hints", "✓ Complete"],
            ["Word Management", "Add/remove words dynamically", "✓ Complete"]
        ]
        
        hangman_table = Table(hangman_features, colWidths=[1.5*inch, 2.5*inch, 1*inch])
        hangman_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(hangman_table)
        story.append(Spacer(1, 20))
        
        story.append(Paragraph("<b>Files Created:</b>", self.styles['Normal']))
        story.append(Paragraph("• hangman.py - Basic game implementation", self.styles['Normal']))
        story.append(Paragraph("• enhanced_hangman.py - Advanced features", self.styles['Normal']))
        story.append(Paragraph("• word_manager.py - Word management system", self.styles['Normal']))
        story.append(Paragraph("• README.md - Documentation", self.styles['Normal']))
        story.append(PageBreak())
        
        # Task 2: Web Scraper
        story.append(Paragraph("Task 2: Web Scraper (Intermediate Level)", self.heading_style))
        story.append(Paragraph("<b>Objective:</b> Extract data from websites and save in multiple formats", self.styles['Normal']))
        story.append(Spacer(1, 12))
        
        scraper_features = [
            ["Feature", "Implementation", "Status"],
            ["News Headlines", "BBC News scraping", "✓ Complete"],
            ["Quote Extraction", "Quotes to Scrape website", "✓ Complete"],
            ["Data Export", "CSV and JSON formats", "✓ Complete"],
            ["Error Handling", "Robust exception management", "✓ Complete"],
            ["Multiple Sources", "Configurable target websites", "✓ Complete"],
            ["Scrapy Integration", "Professional scraping framework", "✓ Complete"]
        ]
        
        scraper_table = Table(scraper_features, colWidths=[1.5*inch, 2.5*inch, 1*inch])
        scraper_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(scraper_table)
        story.append(Spacer(1, 20))
        
        story.append(Paragraph("<b>Files Created:</b>", self.styles['Normal']))
        story.append(Paragraph("• scraper.py - Main scraping engine", self.styles['Normal']))
        story.append(Paragraph("• scrapy_spiders.py - Scrapy framework implementation", self.styles['Normal']))
        story.append(Paragraph("• requirements.txt - Dependencies", self.styles['Normal']))
        story.append(Paragraph("• README.md - Documentation", self.styles['Normal']))
        story.append(PageBreak())
        
        # Task 3: Cricket Fielding Analysis
        story.append(Paragraph("Task 3: Cricket Fielding Analysis (Advanced Level)", self.heading_style))
        story.append(Paragraph("<b>Objective:</b> Comprehensive cricket fielding performance analysis system", self.styles['Normal']))
        story.append(Spacer(1, 12))
        
        cricket_features = [
            ["Component", "Implementation", "Status"],
            ["Data Collection", "Interactive and programmatic entry", "✓ Complete"],
            ["Performance Metrics", "Catch rate, run-out rate, efficiency", "✓ Complete"],
            ["Player Analysis", "Individual performance breakdown", "✓ Complete"],
            ["Team Analysis", "Team-wide fielding summary", "✓ Complete"],
            ["Data Export", "CSV and JSON formats", "✓ Complete"],
            ["Visualization", "Charts and performance graphs", "✓ Complete"],
            ["Sample Data", "India vs Australia T20 match", "✓ Complete"]
        ]
        
        cricket_table = Table(cricket_features, colWidths=[1.5*inch, 2.5*inch, 1*inch])
        cricket_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkorange),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(cricket_table)
        story.append(Spacer(1, 20))
        
        # Performance Results
        story.append(Paragraph("<b>Analysis Results:</b>", self.styles['Normal']))
        
        performance_data = [
            ["Player", "Events", "Catch Rate", "Run-out Rate", "Net Impact", "Efficiency"],
            ["Ravindra Jadeja", "4", "100%", "100%", "+16 runs", "75%"],
            ["Virat Kohli", "4", "100%", "50%", "+1 runs", "50%"],
            ["Hardik Pandya", "4", "50%", "0%", "-5 runs", "25%"]
        ]
        
        performance_table = Table(performance_data, colWidths=[1.2*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch])
        performance_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(performance_table)
        story.append(Spacer(1, 20))
        
        story.append(Paragraph("<b>Files Created:</b>", self.styles['Normal']))
        story.append(Paragraph("• fielding_analyzer.py - Core analysis engine", self.styles['Normal']))
        story.append(Paragraph("• data_collector.py - Interactive data collection", self.styles['Normal']))
        story.append(Paragraph("• visualizer.py - Performance visualization", self.styles['Normal']))
        story.append(Paragraph("• requirements.txt - Dependencies", self.styles['Normal']))
        story.append(Paragraph("• README.md - Comprehensive documentation", self.styles['Normal']))
        story.append(PageBreak())
        
        # Summary
        story.append(Paragraph("Project Summary", self.heading_style))
        
        summary_data = [
            ["Metric", "Value"],
            ["Total Projects", "3"],
            ["Programming Languages", "Python"],
            ["Total Files Created", "15+"],
            ["GitHub Repository", "https://github.com/sach200/shadow-fox-internship"],
            ["Documentation", "Complete README files for each project"],
            ["Code Quality", "Clean, modular, well-commented"],
            ["Functionality", "All projects fully functional"],
            ["Complexity Progression", "Beginner → Intermediate → Advanced"]
        ]
        
        summary_table = Table(summary_data, colWidths=[2*inch, 4*inch])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(summary_table)
        story.append(Spacer(1, 30))
        
        # Conclusion
        story.append(Paragraph("<b>Conclusion:</b>", self.styles['Normal']))
        story.append(Paragraph("Successfully completed all three tasks demonstrating progression from basic programming concepts to advanced data analysis and visualization. Each project showcases different aspects of Python development including game logic, web scraping, data analysis, and system design.", self.styles['Normal']))
        
        # Build PDF
        doc.build(story)
        print(f"PDF report generated: {filename}")
        return filename

if __name__ == "__main__":
    generator = TaskReportGenerator()
    generator.create_report()