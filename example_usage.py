#!/usr/bin/env python3
"""
AudioMap Example Usage

This script demonstrates various ways to use the AudioMap library
for audio device mapping with UID support across different platforms.
"""

def main():
    print("AudioMap Package Usage Examples")
    print("=" * 50)
    
    try:
                # Import the audio device detection library
        from audiomap import (
            AudioDeviceDetector,
            list_audio_input_devices,
            list_audio_output_devices,
            get_audio_device_count,
            find_audio_device
        )
        
        print("✅ Package imported successfully!")
        
        # Basic usage
        print("\n📱 Basic Usage Examples:")
        print("-" * 20)
        
        # Use utility functions
        input_devices = list_audio_input_devices()
        output_devices = list_audio_output_devices()
        
        print(f"Input devices: {len(input_devices)} devices")
        print(f"Output devices: {len(output_devices)} devices")
        
        # Show device UIDs
        print("\n📋 Device UID Examples:")
        if input_devices:
            device = input_devices[0]
            print(f"First input device:")
            print(f"  Name: {device['name']}")
            print(f"  UID: {device['id']}")
            print(f"  Platform: {device['platform']}")
        
        if output_devices:
            device = output_devices[0]
            print(f"First output device:")
            print(f"  Name: {device['name']}")
            print(f"  UID: {device['id']}")
            print(f"  Platform: {device['platform']}")
        
        # Use statistics function
        stats = get_audio_device_count()
        print(f"\nTotal: {stats['total']} devices")
        
        # Class interface examples
        print("\n🔧 Class Interface Examples:")
        print("-" * 20)
        
        detector = AudioDeviceDetector()
        platform = detector.current_platform
        print(f"Current platform: {platform}")
        
        # Search examples
        print("\n🔍 Device Search Examples:")
        print("-" * 20)
        
        # Search for built-in devices
        if platform == "Darwin":
            builtin_devices = find_audio_device("MacBook")
        elif platform == "Windows":
            builtin_devices = find_audio_device("Speakers")
        else:
            builtin_devices = find_audio_device("default")
        
        if builtin_devices:
            print(f"Found {len(builtin_devices)} built-in devices")
            for device in builtin_devices[:2]:  # Only show first two
                print(f"  - {device['name']}")
        
        # Error handling examples
        print("\n⚠️ Error Handling Examples:")
        print("-" * 20)
        
        from audiomap.exceptions import AudioDetectionError
        
        try:
            # Here you can try some operations that might fail
            all_devices = detector.list_all_devices()
            print("✅ Device detection working normally")
        except AudioDetectionError as e:
            print(f"❌ Detection error: {e}")
        
        print("\n🎉 All examples executed successfully!")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("\nSuggested solutions:")
        print("1. Ensure package is installed: pip install -e .")
        print("2. Check Python path")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
