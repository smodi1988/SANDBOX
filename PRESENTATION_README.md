# Migration Presentation Generator

This script creates a PowerPoint presentation for the EDWH to EDP Migration Success Story for the Informatica EMEA Master Class session.

## Overview

The presentation covers the migration journey from:
- **Informatica PowerCenter** to **IDMC** (Informatica Intelligent Data Management Cloud)
- **Teradata** to **BigQuery** (BQ)

## Generated Presentation

The script generates: `EDWH_to_EDP_Migration_Success_Story.pptx`

### Presentation Structure (13 Slides)

1. **Title Slide** - EDWH to EDP Migration Success Story
2. **Introduction - Sunrise** - Company overview
3. **Introduction - EDWH** - Legacy architecture overview
4. **EDWH Architecture Landscape** - Detailed architecture components
5. **Migration Needs** - Reasons for migration
6. **Challenges Faced** - Migration challenges
7. **Solution - Assessment & Planning** - Initial phase of migration
8. **Solution - Development & Testing** - Parallel development and DVT
9. **Solution - Tools & Technologies** - Google APIs, IDMC, BigQuery
10. **Benefits Realized** - Processing efficiency, cost savings, PDO
11. **Future Outlook - Innovations** - CLAIRGPT and utilities
12. **Future Outlook - IDMC Topics** - Operational improvements and DevOps
13. **Conclusion** - Summary and closing

## Requirements

Install the required Python package:

```bash
pip install python-pptx
```

Or install all dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Generate the Presentation

Simply run the script:

```bash
python3 create_migration_presentation.py
```

This will create `EDWH_to_EDP_Migration_Success_Story.pptx` in the current directory.

### Customize the Presentation

To customize the presentation content:

1. Open `create_migration_presentation.py` in a text editor
2. Modify the content in the relevant slide creation sections
3. Run the script again to regenerate the presentation

### Example Customization

To add or modify bullet points on a slide, locate the relevant `create_content_slide()` call and update the list. For example:

```python
create_content_slide(prs, "Your Slide Title", [
    "First bullet point",
    "Second bullet point",
    ("Main point with sub-points:", [
        "Sub-point 1",
        "Sub-point 2"
    ])
])
```

## Key Topics Covered

### Migration Journey
- Assessment and planning
- Cloudification strategy
- Parallel development approach
- Environment setup and parallel runs
- Data Validation Tool (DVT)
- Google API for query conversion

### Benefits
- Processing efficiency improvements
- Cost savings
- Push Down Optimization (PDO) on all mappings

### Future Outlook
- CLAIRGPT integration
- Additional utilities
- IDMC operational topics (metadata, Salesforce merge transformations)
- Assessment methodology improvements
- Pipeline parallel execution
- Bitbucket and deployment automation

## Notes

- The presentation uses a standard PowerPoint template
- All slides use a consistent bullet-point format
- You can further refine the presentation in PowerPoint after generation
- Images, charts, and detailed diagrams should be added manually in PowerPoint

## Support

For modifications or issues with the script, please refer to the [python-pptx documentation](https://python-pptx.readthedocs.io/).
