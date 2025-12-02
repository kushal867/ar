from django.core.management.base import BaseCommand
from game.models import POI


class Command(BaseCommand):
    help = 'Seed initial POI data for AR Campus Hunt'

    def handle(self, *args, **kwargs):
        # Clear existing POIs
        POI.objects.all().delete()
        
        # Create POIs
        pois = [
            {
                'name': 'Main Entrance',
                'description': 'Start your journey at the main entrance of Virinchi College',
                'lat': 27.7172,
                'lon': 85.3240,
                'secret_word': 'Kickstart',
                'sequence_order': 1,
                'icon': '🚪'
            },
            {
                'name': 'Robo Soccer Zone',
                'description': 'Find the robots playing soccer',
                'lat': 27.7173,
                'lon': 85.3241,
                'secret_word': 'Sensors',
                'sequence_order': 2,
                'icon': '🤖'
            },
            {
                'name': 'IoT Project Exhibition',
                'description': 'Explore the IoT innovations',
                'lat': 27.7174,
                'lon': 85.3242,
                'secret_word': 'SmartHub',
                'sequence_order': 3,
                'icon': '💡'
            },
            {
                'name': 'Library',
                'description': 'Visit the knowledge center',
                'lat': 27.7175,
                'lon': 85.3243,
                'secret_word': 'Compile',
                'sequence_order': 4,
                'icon': '📚'
            },
            {
                'name': 'Computer Lab',
                'description': 'Where the magic happens',
                'lat': 27.7176,
                'lon': 85.3244,
                'secret_word': 'Applause',
                'sequence_order': 5,
                'icon': '💻'
            },
            {
                'name': 'Main Stage (Final)',
                'description': 'The final destination',
                'lat': 27.7177,
                'lon': 85.3245,
                'secret_word': 'Innovate',
                'sequence_order': 6,
                'icon': '🎯'
            }
        ]
        
        for poi_data in pois:
            POI.objects.create(**poi_data)
            self.stdout.write(
                self.style.SUCCESS(f'Created POI: {poi_data["name"]}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(pois)} POIs')
        )
